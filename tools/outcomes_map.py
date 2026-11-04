"""Build the detailed course-outline alignment page (Front Matter). python3 tools/outcomes_map.py > sections/front_alignment.html"""
import re, html
ID = {}
for l in open('tools/section_ids.txt'):
    m = re.match(r'(\d+) (\d+\.\d+):', l)
    if m: ID[m.group(2)] = int(m.group(1))
ID.update({'4.10': 597099, '7.11': 597131, '11.7': 597172, '12.9': 597183, '13.7': 597194, '13.8': 597195, '13.9': 597196,
           '13.10': 597197, '14.5': 597204, '15.6': 597212, '15.11': 597217})
TITLE = {}
for l in open('tools/section_ids.txt'):
    m = re.match(r'(\d+) (\d+\.\d+): (.*)', l.strip())
    if m: TITLE[m.group(2)] = m.group(3)
TITLE.update({'4.10': 'Acidity of Alcohols and Phenols', '7.11': 'Neurotransmitters', '11.7': 'Enzyme Regulation - Covalent Modification and Genetic Control',
    '12.9': 'Structure and Function of RNA', '13.7': 'Entry of Other Sugars into Glycolysis', '13.8': 'Regulation of Glucose Metabolism and Metabolism During Stress',
    '13.9': 'Glycogen Metabolism- Glycogenesis and Glycogenolysis', '13.10': 'Gluconeogenesis- Glucose Synthesis from Noncarbohydrates',
    '14.5': 'Energy Output in Complete Glucose Catabolism', '15.6': 'Storage and Mobilization of Triacylglycerols', '15.11': 'Biosynthesis of Nonessential Amino Acids'})
def L(nums):
    return ', '.join(f'<a href="/@go/page/{ID[n]}" title="{html.escape(TITLE[n])}">{n}</a>' for n in nums.split())

UNITS = [
 ('1', 'Organic Compounds', [
  ('1.1', 'Representations: Lewis, condensed, expanded and line (skeletal) structures', '1.3 1.7 2.4'),
  ('1.2', 'Shape and polarity: shapes for 2&ndash;4 electron groups, bond angles, bond and molecular polarity', '1.4 1.5'),
  ('1.3', 'Functional groups', '1.6 2.1 4.1')]),
 ('2', 'Alkanes, Alkenes and Alkynes', [
  ('2.1', 'Classification of carbons (1&deg;, 2&deg;, 3&deg;, 4&deg;)', '2.4'),
  ('2.2', 'Saturated and unsaturated hydrocarbons', '2.2 3.1'),
  ('2.3', 'Isomers and conformers (constitutional, cis&ndash;trans; rotation about single bonds; nonplanar rings)', '2.3 2.9 3.2'),
  ('2.4', 'IUPAC nomenclature (-ane, -ene, -yne; cyclic; halogen and alkyl substituents)', '2.5 2.8 2.9 3.1 3.6'),
  ('2.5', 'Physical properties and intermolecular forces (ranking mp, bp, solubility)', '1.8 2.6 3.3'),
  ('2.6', 'Types of reactions: addition, substitution, elimination', '3.4 3.7 4.5'),
  ('2.7', 'Reactions of alkanes: combustion, halogenation', '2.7'),
  ('2.8', 'Reactions of alkenes: hydrogenation, halogenation, hydrohalogenation, hydration (Markovnikov&rsquo;s rule)', '3.4'),
  ('2.9', 'Polymers', '3.5')]),
 ('3', 'Aromatic Compounds', [
  ('3.1&ndash;3.4', 'Benzene structure, naming (ortho/meta/para, phenyl), physical properties, polycyclic aromatic hydrocarbons', '3.7 3.8'),
  ('3.5', 'Reactions of benzene: halogenation, nitration, sulfonation', '3.7')]),
 ('4', 'Alcohols, Phenols, Thiols and Ethers', [
  ('4.1', 'Classification of alcohols; constitutional isomers', '4.1 4.2'),
  ('4.2', 'Nomenclature of alcohols, phenols, ethers and thiols', '4.2 4.6 4.7 4.8 4.9'),
  ('4.3', 'Physical properties; acidity of alcohols vs phenols', '4.3 4.10'),
  ('4.4', 'Dehydration (Zaitsev&rsquo;s rule, Le Chatelier); oxidation of alcohols and thiols', '4.4 4.5 4.9')]),
 ('5', 'Aldehydes and Ketones', [
  ('5.1&ndash;5.2', 'Carbonyl structures and nomenclature', '5.1'),
  ('5.3', 'Physical properties', '5.2'),
  ('5.4', 'Oxidation and reduction (Tollens&rsquo;, Benedict&rsquo;s); hemiacetals and acetals; hydrolysis', '5.3 5.4')]),
 ('6', 'Chirality', [
  ('6.1&ndash;6.4', 'Handedness, chiral centers, enantiomers and diastereomers, Fischer projections, D/L', '5.5')]),
 ('7', 'Carboxylic Acids and Esters', [
  ('7.1&ndash;7.2', 'Acyl groups; nomenclature of acids and esters', '6.1 6.5'),
  ('7.3', 'Physical properties; acidity and carboxylate salts', '6.3 6.4 6.6 6.10'),
  ('7.4', 'Neutralization; Fischer esterification', '6.4 6.7'),
  ('7.5', 'Ester hydrolysis: acid-catalyzed and saponification', '6.8 6.9')]),
 ('8', 'Amines and Amides', [
  ('8.1, 8.3', 'Classification and nomenclature of amines and amides', '7.1 7.4'),
  ('8.2', 'Heterocyclic amines', '7.8 7.9'),
  ('8.4&ndash;8.5', 'Physical properties; basicity, ammonium salts, neutralization', '7.2 7.3 7.5'),
  ('8.6&ndash;8.7', 'Amidation; amide hydrolysis', '7.6 7.7'),
  ('8.8', 'Neurotransmitters', '7.11'),
  ('8.9', 'Functional groups in macromolecules (polyesters, polyamides, peptides)', '7.10 10.4')]),
 ('9', 'Carbohydrates', [
  ('9.1&ndash;9.2', 'Classifying monosaccharides; Fischer and Haworth projections; anomers, mutarotation', '8.2 8.4'),
  ('9.3&ndash;9.4', 'Physical properties; glucose, galactose, fructose', '8.1 8.3'),
  ('9.5', 'Oxidation and reduction of monosaccharides; reducing sugars; sugar alcohols', '8.5'),
  ('9.6', 'Disaccharides and polysaccharides; glycosidic linkages', '8.6 8.7')]),
 ('10', 'Lipids', [
  ('10.1', 'Properties of lipids', '9.2'),
  ('10.2', 'Steroids, fat-soluble vitamins, eicosanoids', '9.1 9.6 11.5'),
  ('10.3', 'Fatty acids, waxes, triacylglycerols (hydrogenation, oxidation, saponification)', '9.1 9.2'),
  ('10.4', 'Glycerolipids, phospholipids, sphingolipids; membranes and transport', '9.3 9.4 9.5')]),
 ('11', 'Amino Acids and Proteins', [
  ('11.1', 'Amino acid structure, R-group classes, abbreviations, D/L', '10.1'),
  ('11.2', 'Zwitterions and isoelectric point', '10.2'),
  ('11.3', 'Peptide bonds, hydrolysis, naming peptides', '10.3 10.4'),
  ('11.4', 'Primary, secondary, tertiary and quaternary structure', '10.6 10.7 10.8 10.9'),
  ('11.5', 'Protein hydrolysis and denaturation', '10.10')]),
 ('12', 'Enzymes and Vitamins', [
  ('12.1', 'Catalysis, specificity, models of enzyme action', '11.1 11.2'),
  ('12.2', 'Enzyme classes', '11.1'),
  ('12.3', 'pH, temperature, concentration; allosteric, feedback and covalent control; inhibition; cofactors and vitamins', '11.3 11.4 11.5 11.6 11.7')]),
 ('13', 'Nucleic Acids and Protein Synthesis', [
  ('13.1&ndash;13.2', 'Components; DNA vs RNA structure; types of RNA', '12.1 12.2 12.9'),
  ('13.3', 'DNA replication', '12.3'),
  ('13.4', 'Transcription, translation and the genetic code', '12.4 12.5'),
  ('13.5', 'Mutations', '12.6'),
  ('13.6&ndash;13.7', 'Recombinant DNA; viruses', '12.7 12.8')]),
 ('14', 'Metabolic Pathways for Carbohydrates', [
  ('14.1', 'Stages of metabolism, catabolism and anabolism, coenzymes', '13.1 13.2 13.4'),
  ('14.2', 'Digestion of carbohydrates', '13.3'),
  ('14.3', 'Glycolysis: reaction types, enzyme classes, coenzymes, regulation', '13.6 13.7 13.8'),
  ('14.4', 'Fates of pyruvate (aerobic and anaerobic)', '13.5 14.1'),
  ('14.5', 'Pentose phosphate pathway', '13.7'),
  ('14.6', 'Glycogenesis and glycogenolysis', '13.9'),
  ('14.7', 'Gluconeogenesis; Cori cycle; regulation', '13.5 13.10')]),
 ('15', 'Metabolism and Energy', [
  ('15.1', 'Citric acid cycle', '14.3'),
  ('15.2', 'Electron transport and oxidative phosphorylation', '14.2 14.4'),
  ('15.3', 'Net ATP from glucose (including the malate&ndash;aspartate shuttle)', '14.5')]),
 ('16', 'Metabolic Pathways for Lipids', [
  ('16.1&ndash;16.2', 'Digestion of triacylglycerols; fat storage and mobilization; glycerol metabolism', '15.1 15.5 15.6'),
  ('16.3', 'Fatty acid activation, carnitine shuttle, &beta;-oxidation, net ATP', '15.3'),
  ('16.4', 'Ketone bodies', '15.7'),
  ('16.5', 'Fatty acid synthesis (lipogenesis)', '15.8')]),
 ('17', 'Metabolic Pathways for Amino Acids', [
  ('17.1&ndash;17.2', 'Protein digestion; amino acid pool; nitrogen balance', '15.2 15.9'),
  ('17.3', 'Transamination, oxidative deamination, urea cycle, carbon skeletons', '15.4 15.10'),
  ('17.4', 'Essential and nonessential amino acids', '10.1 15.11')]),
]
OBJ = [
 ('Perform structural formula-to-name conversions for organic and biochemical compounds.', '2.5 3.1 3.8 4.2 5.1 6.1 6.5 7.1 7.4 10.4'),
 ('Describe physical properties of organic compounds.', '1.8 2.6 3.3 4.3 5.2 6.3 6.6 7.2 7.5'),
 ('Predict products of representative chemical reactions.', '2.7 3.4 4.5 5.3 5.4 6.7 6.8 7.6 7.7'),
 ('Describe the major organic functional groups and identify the major categories of biological compounds.', '1.6 4.1 8.1 9.1 10.1 12.1'),
 ('Organize and illustrate the function and processes that enzymes and coenzymes perform in each of the major metabolic pathways.', '11.5 13.1 13.6 13.9 13.10 14.3 14.4 15.3 15.10'),
 ('Compare and contrast DNA replication, transcription, RNA translation, and common types of mutation.', '12.3 12.4 12.5 12.6'),
]
o = ['<p>This page maps every topic in the Fresno City College course outline of record for CHEM 3B (effective Spring 2027, C-ID CHEM 102) to the sections of this book that teach it. Instructors and reviewers can use it to check coverage; students can use it to find the reading for any topic on the syllabus. Each chapter also has a Chapter Guide, Practice Problems and Practice Games that cover the same topics. The chapter-level summary and the student learning outcomes are on the <a href="/@go/page/597270">About This Book</a> page.</p>']
o.append('<h2>Course objectives</h2>')
o.append('<table class="mt-responsive-table"><caption>CHEM 3B course objectives and the sections that teach them</caption><thead><tr><th scope="col">Course objective</th><th scope="col">Sections</th></tr></thead><tbody>')
for i, (t, n) in enumerate(OBJ, 1):
    o.append(f'<tr><td data-th="Course objective">{i}. {t}</td><td data-th="Sections">{L(n)}</td></tr>')
o.append('</tbody></table>')
o.append('<h2>Lecture topics</h2>')
for u, name, items in UNITS:
    o.append(f'<h3>Outline unit {u}: {name}</h3>')
    o.append(f'<table class="mt-responsive-table"><caption>Outline unit {u} topics and book sections</caption><thead><tr><th scope="col">Outline item</th><th scope="col">Topic</th><th scope="col">Book sections</th></tr></thead><tbody>')
    for code, topic, n in items:
        o.append(f'<tr><td data-th="Outline item">{code}</td><td data-th="Topic">{topic}</td><td data-th="Book sections">{L(n)}</td></tr>')
    o.append('</tbody></table>')
o.append('<h2>Laboratory</h2><p>The outline&rsquo;s laboratory topics are taught in the CHEM 3B lab manual. Each chapter&rsquo;s &ldquo;In the Lab&rdquo; boxes connect the reading to those experiments.</p>')
print('\n'.join(o))

---
entity_id: "molecule.C00025"
entity_type: "small_molecule"
name: "L-Glutamate"
source_database: "KEGG"
source_id: "C00025"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Glutamate"
  - "L-Glutamic acid"
  - "L-Glutaminic acid"
  - "Glutamate"
---

# L-Glutamate

`molecule.C00025`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00025`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Glutamate; L-Glutamic acid; L-Glutaminic acid; Glutamate GLT is one of the proteinogenic amino acids. It is named after wheat gluten, from which it was described in 1866 by the German chemist Karl Heinrich Ritthausen. GLT plays an important role in nitrogen metabolism in the cell. Once cells take up ammonium, it is fixed by incorporation into the TCA cycle intermediate 2-KETOGLUTARATE by EC-1.4.1.4, forming GLT (an additional ammonium molecule can be fixed into L-glutamate, e.g. by EC-6.3.1.2, forming GLN ). Glutamate then becomes the central source for passing amino groups on to other molecules by the action of transaminase (=aminotransferase) enzymes, distributing nitrogen throughout the cell. For example, glutamate can transfer the amino group to the common metabolites PYRUVATE and OXALACETIC_ACID, forming L-ALPHA-ALANINE and L-ASPARTATE, respectively. It has been estimated that glutamate and glutamine provide 75% and 25%, respectively, of all cellular nitrogen . In addition to its protein building role, GLT is the most abundant excitatory neurotransmitter in the vertebrate nervous system, acting on ionotropic and metabotropic (G-protein coupled) receptors . GLT interacts with the umami taste receptors, which sense glutamates and nucleotides, imparting "meaty", "savory", and "broth-like" flavor...

## Biological Role

Consumed as substrate in 31 reaction(s). Produced in 68 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: L-Glutamate; L-Glutamic acid; L-Glutaminic acid; Glutamate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (104)

- `activates` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-10427|complex.ecocyc.CPLX0-10427]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00245|reaction.R00245]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_product_of` --> [[reaction.R00251|reaction.R00251]] `KEGG` `database` - C00002 + C01879 + 2 C00001 <=> C00008 + C00009 + C00025
- `is_product_of` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014
- `is_product_of` --> [[reaction.R00258|reaction.R00258]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025
- `is_product_of` --> [[reaction.R00355|reaction.R00355]] `KEGG` `database` - C00049 + C00026 <=> C00036 + C00025
- `is_product_of` --> [[reaction.R00411|reaction.R00411]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_product_of` --> [[reaction.R00494|reaction.R00494]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_product_of` --> [[reaction.R00573|reaction.R00573]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_product_of` --> [[reaction.R00575|reaction.R00575]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_product_of` --> [[reaction.R00578|reaction.R00578]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_product_of` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_product_of` --> [[reaction.R00707|reaction.R00707]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_product_of` --> [[reaction.R00708|reaction.R00708]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_product_of` --> [[reaction.R00734|reaction.R00734]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_product_of` --> [[reaction.R00768|reaction.R00768]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_product_of` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_product_of` --> [[reaction.R01155|reaction.R01155]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_product_of` --> [[reaction.R02619|reaction.R02619]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_product_of` --> [[reaction.R04438|reaction.R04438]] `KEGG` `database` - C04346 + C00026 <=> C11907 + C00025
- `is_product_of` --> [[reaction.ecocyc.2.6.1.57-RXN|reaction.ecocyc.2.6.1.57-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.6.1.7-RXN|reaction.ecocyc.2.6.1.7-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2.6.1.82-RXN|reaction.ecocyc.2.6.1.82-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN|reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ABC-13-RXN|reaction.ecocyc.ABC-13-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIAMTRANSAM-RXN|reaction.ecocyc.DIAMTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FGAMSYN-RXN|reaction.ecocyc.FGAMSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTAMIN-RXN|reaction.ecocyc.GLUTAMIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GMP-SYN-GLUT-RXN|reaction.ecocyc.GMP-SYN-GLUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HISTAMINOTRANS-RXN|reaction.ecocyc.HISTAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAD-SYNTH-GLN-RXN|reaction.ecocyc.NAD-SYNTH-GLN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PABASYN-RXN|reaction.ecocyc.PABASYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PSERTRANSAM-RXN|reaction.ecocyc.PSERTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PSERTRANSAMPYR-RXN|reaction.ecocyc.PSERTRANSAMPYR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PUTTRANSAM-RXN|reaction.ecocyc.PUTTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN|reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RFFTRANS-RXN|reaction.ecocyc.RFFTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12618|reaction.ecocyc.RXN-12618]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14116|reaction.ecocyc.RXN-14116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21858|reaction.ecocyc.RXN-21858]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1863|reaction.ecocyc.RXN0-1863]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3942|reaction.ecocyc.RXN0-3942]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5040|reaction.ecocyc.RXN0-5040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6981|reaction.ecocyc.RXN0-6981]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6984|reaction.ecocyc.RXN0-6984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7317|reaction.ecocyc.RXN0-7317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCGLUDESUCC-RXN|reaction.ecocyc.SUCCGLUDESUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SUCCORNTRANSAM-RXN|reaction.ecocyc.SUCCORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-122|reaction.ecocyc.TRANS-RXN-122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-162|reaction.ecocyc.TRANS-RXN-162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-261|reaction.ecocyc.TRANS-RXN-261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00114|reaction.R00114]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00239|reaction.R00239]] `KEGG` `database` - C00002 + C00025 <=> C00008 + C03287
- `is_substrate_of` --> [[reaction.R00248|reaction.R00248]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00253|reaction.R00253]] `KEGG` `database` - C00002 + C00025 + C00014 <=> C00008 + C00009 + C00064
- `is_substrate_of` --> [[reaction.R00259|reaction.R00259]] `KEGG` `database` - C00024 + C00025 <=> C00010 + C00624
- `is_substrate_of` --> [[reaction.R00260|reaction.R00260]] `KEGG` `database` - C00025 <=> C00217
- `is_substrate_of` --> [[reaction.R00261|reaction.R00261]] `KEGG` `database` - C00025 <=> C00334 + C00011
- `is_substrate_of` --> [[reaction.ecocyc.ABC-13-RXN|reaction.ecocyc.ABC-13-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROFOLATESYNTH-RXN|reaction.ecocyc.DIHYDROFOLATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN|reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLURS-RXN|reaction.ecocyc.GLURS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTCYSLIG-RXN|reaction.ecocyc.GLUTCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTKIN-RXN|reaction.ecocyc.GLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTRACE-RXN|reaction.ecocyc.GLUTRACE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18804|reaction.ecocyc.RXN-18804]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20084|reaction.ecocyc.RXN-20084]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2921|reaction.ecocyc.RXN0-2921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3901|reaction.ecocyc.RXN0-3901]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5422|reaction.ecocyc.RXN0-5422]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6726|reaction.ecocyc.RXN0-6726]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7448|reaction.ecocyc.RXN0-7448]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-122|reaction.ecocyc.TRANS-RXN-122]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-162|reaction.ecocyc.TRANS-RXN-162]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-261|reaction.ecocyc.TRANS-RXN-261]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-13-CPLX|complex.ecocyc.ABC-13-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AER8|protein.P0AER8]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P21345|protein.P21345]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00025`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

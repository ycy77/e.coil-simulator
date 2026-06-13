---
entity_id: "protein.P17443"
entity_type: "protein"
name: "murG"
source_database: "UniProt"
source_id: "P17443"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:1649817, ECO:0000269|PubMed:17640276, ECO:0000269|PubMed:8449890}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:1649817, ECO:0000269|PubMed:17640276, ECO:0000269|PubMed:8449890}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:8449890}. Note=Randomly distributed in the cell envelope with a higher intensity at the division site. Mid-cell localization requires divisome components. {ECO:0000269|PubMed:17640276}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murG b0090 JW0088"
---

# murG

`protein.P17443`

## Static

- Type: `protein`
- Source: `UniProt:P17443`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:1649817, ECO:0000269|PubMed:17640276, ECO:0000269|PubMed:8449890}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:1649817, ECO:0000269|PubMed:17640276, ECO:0000269|PubMed:8449890}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_00033, ECO:0000269|PubMed:8449890}. Note=Randomly distributed in the cell envelope with a higher intensity at the division site. Mid-cell localization requires divisome components. {ECO:0000269|PubMed:17640276}.

## Enriched Summary

FUNCTION: Cell wall formation (PubMed:1649817). Catalyzes the transfer of a GlcNAc subunit on undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide (lipid intermediate I) to form undecaprenyl-pyrophosphoryl-MurNAc-(pentapeptide)GlcNAc (lipid intermediate II) (PubMed:12538870, PubMed:1649817). Strongly prefers UDP to CDP, GDP, ADP and TDP (PubMed:12538870). {ECO:0000269|PubMed:12538870, ECO:0000269|PubMed:1649817}. The murG gene codes for the N-acetylglucosaminyl transferase responsible for the final intracellular step of peptidoglycan subunit assembly. The transferase is associated with the cytoplasmic face of the inner membrane. Therefore, the entire peptidoglycan subunit is assembled before transport across the cytoplasmic membrane . The crystal structures of MurG by itself to a resolution of 1.9 Å and in a complex with its substrate UDP-GlcNAc to a resolution of 2.5 Å have been determined by X-ray crystallography. A temperature sensitive MurG mutant fails to localize to cell-division sites resulting in cell lysis . Mid-cell localization of MurG during cell division was dependent upon the presence of a mature divisome including the proteins FtsZ, PBP3, FtsW, FtsQ, MreC, and MreD, but did not depend upon MreB...

## Biological Role

Catalyzes R06172 (reaction.R06172), R06173 (reaction.R06173), R06174 (reaction.R06174), UDP-N-acetyl-D-glucosamine:N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine-diphosphoundecaprenol 4-β-N-acetylglucosaminlytransferase (reaction.ecocyc.NACGLCTRANS-RXN).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Cell wall formation (PubMed:1649817). Catalyzes the transfer of a GlcNAc subunit on undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide (lipid intermediate I) to form undecaprenyl-pyrophosphoryl-MurNAc-(pentapeptide)GlcNAc (lipid intermediate II) (PubMed:12538870, PubMed:1649817). Strongly prefers UDP to CDP, GDP, ADP and TDP (PubMed:12538870). {ECO:0000269|PubMed:12538870, ECO:0000269|PubMed:1649817}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06172|reaction.R06172]] `KEGG` `database` - via EC:2.4.1.227
- `catalyzes` --> [[reaction.R06173|reaction.R06173]] `KEGG` `database` - via EC:2.4.1.227
- `catalyzes` --> [[reaction.R06174|reaction.R06174]] `KEGG` `database` - via EC:2.4.1.227
- `catalyzes` --> [[reaction.ecocyc.NACGLCTRANS-RXN|reaction.ecocyc.NACGLCTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0090|gene.b0090]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17443`
- `KEGG:ecj:JW0088;eco:b0090;ecoc:C3026_00355;`
- `GeneID:946321;`
- `GO:GO:0005886; GO:0005975; GO:0008360; GO:0009252; GO:0050511; GO:0051301; GO:0051991; GO:0071555`
- `EC:2.4.1.227`

## Notes

UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC 2.4.1.227) (Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc GlcNAc transferase)

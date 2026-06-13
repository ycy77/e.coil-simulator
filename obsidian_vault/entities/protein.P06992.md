---
entity_id: "protein.P06992"
entity_type: "protein"
name: "rsmA"
source_database: "UniProt"
source_id: "P06992"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmA ksgA b0051 JW0050"
---

# rsmA

`protein.P06992`

## Static

- Type: `protein`
- Source: `UniProt:P06992`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically dimethylates two adjacent adenosines (A1518 and A1519) in the loop of a conserved hairpin near the 3'-end of 16S rRNA in the 30S particle. May play a critical role in biogenesis of 30S subunits. Also has a DNA glycosylase/AP lyase activity that removes C mispaired with oxidized T from DNA, and may play a role in protection of DNA against oxidative stress. {ECO:0000269|PubMed:18990185, ECO:0000269|PubMed:19223326, ECO:0000269|PubMed:3905517}. RsmA is the methyltransferase responsible for dimethylation of 16S rRNA at the two adjacent adenosine bases A1518 and A1519 . In vitro, the enzyme is active on CPLX0-3953 "30S ribosomal subunits", but not the fully assembled 70S CPLX0-3964 . RsmA may play a role in biogenesis of the small subunit of the ribosome , providing a checkpoint where binding of RsmA keeps immature 30S subunits from entering the translational cycle . RsmA and the ribosome maturation factor EG11178-MONOMER RbfA function together in checkpointing maturation of the 30S subunit . Methylation of the 16S rRNA by RsmA is important for release of RbfA from the 30S subunit . The evolutionary relationship and functional divergence of this enzyme and its homologs in eukaryotes has been studied . RsmA as well as the dimethylation modification it catalyzes are nearly universally conserved, suggesting an important function...

## Biological Role

Catalyzes RXN-11633 (reaction.ecocyc.RXN-11633). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Specifically dimethylates two adjacent adenosines (A1518 and A1519) in the loop of a conserved hairpin near the 3'-end of 16S rRNA in the 30S particle. May play a critical role in biogenesis of 30S subunits. Also has a DNA glycosylase/AP lyase activity that removes C mispaired with oxidized T from DNA, and may play a role in protection of DNA against oxidative stress. {ECO:0000269|PubMed:18990185, ECO:0000269|PubMed:19223326, ECO:0000269|PubMed:3905517}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11633|reaction.ecocyc.RXN-11633]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0051|gene.b0051]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06992`
- `KEGG:ecj:JW0050;eco:b0051;ecoc:C3026_00265;`
- `GeneID:93777384;944939;`
- `GO:GO:0000028; GO:0000179; GO:0003690; GO:0003729; GO:0005829; GO:0006364; GO:0030490; GO:0031167; GO:0043024; GO:0046677; GO:0052908; GO:0070475`
- `EC:2.1.1.182`

## Notes

Ribosomal RNA small subunit methyltransferase A (EC 2.1.1.182) (16S rRNA (adenine(1518)-N(6)/adenine(1519)-N(6))-dimethyltransferase) (16S rRNA dimethyladenosine transferase) (16S rRNA dimethylase) (High level kasugamycin resistance protein KsgA) (Kasugamycin dimethyltransferase) (S-adenosylmethionine-6-N', N'-adenosyl(rRNA) dimethyltransferase)

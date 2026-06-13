---
entity_id: "protein.Q59385"
entity_type: "protein"
name: "copA"
source_database: "UniProt"
source_id: "Q59385"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: [Copper-exporting P-type ATPase]: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:12351646}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.; SUBCELLULAR LOCATION: [Isoform Soluble copper chaperone CopA(Z)]: Cytoplasm {ECO:0000305|PubMed:28107647}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "copA atcU f834 ybaR b0484 JW0473"
---

# copA

`protein.Q59385`

## Static

- Type: `protein`
- Source: `UniProt:Q59385`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: [Copper-exporting P-type ATPase]: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:12351646}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.; SUBCELLULAR LOCATION: [Isoform Soluble copper chaperone CopA(Z)]: Cytoplasm {ECO:0000305|PubMed:28107647}.

## Enriched Summary

FUNCTION: [Copper-exporting P-type ATPase]: Exports Cu(+) from the cytoplasm to the periplasm (PubMed:10639134, PubMed:11167016, PubMed:11500054, PubMed:12351646). Binds 2 Cu(+) ions per monomer, which are transferred to periplasmic copper chaperone CusF upon ATP hydrolysis (PubMed:24917681). In vitro an excess of CusF over CopA is required for efficient transfer (PubMed:24917681). May also be involved in silver export (PubMed:12351646, PubMed:12832075). {ECO:0000269|PubMed:10639134, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11500054, ECO:0000269|PubMed:12351646, ECO:0000269|PubMed:12832075, ECO:0000269|PubMed:24917681}.; FUNCTION: [Isoform Soluble copper chaperone CopA(Z)]: mRNA is subject to programmed ribosomal frameshifting which produces a cytoplasmic copper chaperone CopA(Z) that corresponds to the first HMA domain (PubMed:28107647). The soluble form is essential for cell survivial in the presence of CuSO(4); in growth competition experiments between wild-type and a version that prevents expression of CopA(Z) after 50 generations the non-CopA(Z) version is nearly extinct (PubMed:28107647). The first HMA domain (residues 1-70) can be replaced by B.subtilis Cu chaperone CopZ (PubMed:25899340). {ECO:0000269|PubMed:25899340, ECO:0000269|PubMed:28107647}. CopA is a P-type ATPase that catalyses the efflux of monovalent copper in E. coli K-12...

## Biological Role

Catalyzes RXN-14455 (reaction.ecocyc.RXN-14455). Transports Cu+ (molecule.ecocyc.CU_), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: [Copper-exporting P-type ATPase]: Exports Cu(+) from the cytoplasm to the periplasm (PubMed:10639134, PubMed:11167016, PubMed:11500054, PubMed:12351646). Binds 2 Cu(+) ions per monomer, which are transferred to periplasmic copper chaperone CusF upon ATP hydrolysis (PubMed:24917681). In vitro an excess of CusF over CopA is required for efficient transfer (PubMed:24917681). May also be involved in silver export (PubMed:12351646, PubMed:12832075). {ECO:0000269|PubMed:10639134, ECO:0000269|PubMed:11167016, ECO:0000269|PubMed:11500054, ECO:0000269|PubMed:12351646, ECO:0000269|PubMed:12832075, ECO:0000269|PubMed:24917681}.; FUNCTION: [Isoform Soluble copper chaperone CopA(Z)]: mRNA is subject to programmed ribosomal frameshifting which produces a cytoplasmic copper chaperone CopA(Z) that corresponds to the first HMA domain (PubMed:28107647). The soluble form is essential for cell survivial in the presence of CuSO(4); in growth competition experiments between wild-type and a version that prevents expression of CopA(Z) after 50 generations the non-CopA(Z) version is nearly extinct (PubMed:28107647). The first HMA domain (residues 1-70) can be replaced by B.subtilis Cu chaperone CopZ (PubMed:25899340). {ECO:0000269|PubMed:25899340, ECO:0000269|PubMed:28107647}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-14455|reaction.ecocyc.RXN-14455]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0484|gene.b0484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q59385`
- `KEGG:ecj:JW0473;eco:b0484;ecoc:C3026_02380;`
- `GeneID:946106;`
- `GO:GO:0005507; GO:0005524; GO:0005737; GO:0005886; GO:0006825; GO:0010273; GO:0015080; GO:0015662; GO:0016020; GO:0016887; GO:0043682; GO:0055070; GO:0060003; GO:0071280; GO:0071292; GO:0075523; GO:0140581; GO:1902601`
- `EC:7.2.2.8`

## Notes

Copper-exporting P-type ATPase (EC 7.2.2.8) (Copper-exporting P-type ATPase A) (Cu(+)-exporting ATPase) (Soluble copper chaperone CopA(Z))

---
entity_id: "protein.P03004"
entity_type: "protein"
name: "dnaA"
source_database: "UniProt"
source_id: "P03004"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00377, ECO:0000269|PubMed:22574163}. Cytoplasm, nucleoid {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:28166228}. Cell inner membrane {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:9478970}; Peripheral membrane protein {ECO:0000269|PubMed:22574163}. Note=About 10% of the protein associates with the cell inner membrane (shown in strain BL21(DE3)) (PubMed:22574163). 70% of the protein oscillates between opposite cell halves in a time frame of a few seconds, independent of transcription (PubMed:28166228). {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:28166228}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaA b3702 JW3679"
---

# dnaA

`protein.P03004`

## Static

- Type: `protein`
- Source: `UniProt:P03004`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00377, ECO:0000269|PubMed:22574163}. Cytoplasm, nucleoid {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:28166228}. Cell inner membrane {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:9478970}; Peripheral membrane protein {ECO:0000269|PubMed:22574163}. Note=About 10% of the protein associates with the cell inner membrane (shown in strain BL21(DE3)) (PubMed:22574163). 70% of the protein oscillates between opposite cell halves in a time frame of a few seconds, independent of transcription (PubMed:28166228). {ECO:0000269|PubMed:22574163, ECO:0000269|PubMed:28166228}.

## Enriched Summary

FUNCTION: Plays an essential in the initiation and regulation of chromosomal replication. Binds in an ATP-dependent fashion to the origin of replication (oriC) to initiate formation of the DNA replication initiation complex once per cell cycle (PubMed:3036372). Binds the DnaA box (consensus sequence 5'-TTATC[CA]A[CA]A-3') and separates the double-stranded (ds)DNA (PubMed:3036372, PubMed:18216012). Forms a right-handed helical filament on oriC DNA; dsDNA binds to the exterior of the filament while single-stranded (ss)DNA is stabiized in the filament's interior (By similarity). The ATP-DnaA-oriC complex binds and stabilizes the upper strand of the AT-rich DNA unwinding element (DUE) (PubMed:18216012). Mutagenesis of residues that line the central pore blocks dsDNA strand separation (PubMed:18216012). Subsequent binding of DNA polymerase III subunits leads to replisome formation (PubMed:3036372, PubMed:18216012). The DnaA-ATP form converts to DnaA-ADP; once converted to ADP the protein cannot initiate replication, ensuring only 1 round of replication per cell cycle (PubMed:3036372). Binds ATP, ADP and dATP equally well, hydrolyzes ATP with a half-life of about 15 minutes, ATP hydrolysis is not required for pre-priming replisome formation, nucleotide exchange is very slow (PubMed:3036372). Binds acidic phospholipids (PubMed:9478970, PubMed:26272946)...

## Biological Role

Component of DnaA-ATP (complex.ecocyc.MONOMER0-160), DnaA-ADP (complex.ecocyc.MONOMER0-4565).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Plays an essential in the initiation and regulation of chromosomal replication. Binds in an ATP-dependent fashion to the origin of replication (oriC) to initiate formation of the DNA replication initiation complex once per cell cycle (PubMed:3036372). Binds the DnaA box (consensus sequence 5'-TTATC[CA]A[CA]A-3') and separates the double-stranded (ds)DNA (PubMed:3036372, PubMed:18216012). Forms a right-handed helical filament on oriC DNA; dsDNA binds to the exterior of the filament while single-stranded (ss)DNA is stabiized in the filament's interior (By similarity). The ATP-DnaA-oriC complex binds and stabilizes the upper strand of the AT-rich DNA unwinding element (DUE) (PubMed:18216012). Mutagenesis of residues that line the central pore blocks dsDNA strand separation (PubMed:18216012). Subsequent binding of DNA polymerase III subunits leads to replisome formation (PubMed:3036372, PubMed:18216012). The DnaA-ATP form converts to DnaA-ADP; once converted to ADP the protein cannot initiate replication, ensuring only 1 round of replication per cell cycle (PubMed:3036372). Binds ATP, ADP and dATP equally well, hydrolyzes ATP with a half-life of about 15 minutes, ATP hydrolysis is not required for pre-priming replisome formation, nucleotide exchange is very slow (PubMed:3036372). Binds acidic phospholipids (PubMed:9478970, PubMed:26272946). DnaA inhibits its own gene expression (PubMed:2981626) as well as that of other genes including dam, rpoH (PubMed:2540187), ftsA and mioC. {ECO:0000250|UniProtKB:O66659, ECO:0000269|PubMed:18216012, ECO:0000269|PubMed:2540187, ECO:0000269|PubMed:26272946, ECO:0000269|PubMed:2981626, ECO:0000269|PubMed:3036372, ECO:0000269|PubMed:9478970}.; FUNCTION: Also required for replication of some plasmid DNA; binds 4 DnaA boxes in the minimal plasmid RK2 replication origin (oriV). {ECO:0000269|PubMed:15878847, ECO:0000269|PubMed:9242693}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (24)

- `activates` --> [[gene.b2234|gene.b2234]] `RegulonDB` `C` - regulator=DnaA; target=nrdA; function=-+
- `activates` --> [[gene.b2235|gene.b2235]] `RegulonDB` `C` - regulator=DnaA; target=nrdB; function=-+
- `activates` --> [[gene.b2236|gene.b2236]] `RegulonDB` `C` - regulator=DnaA; target=yfaE; function=-+
- `activates` --> [[gene.b3700|gene.b3700]] `RegulonDB` `S` - regulator=DnaA; target=recF; function=-+
- `activates` --> [[gene.b3701|gene.b3701]] `RegulonDB` `C` - regulator=DnaA; target=dnaN; function=-+
- `activates` --> [[gene.b3702|gene.b3702]] `RegulonDB` `S` - regulator=DnaA; target=dnaA; function=-+
- `activates` --> [[gene.b3863|gene.b3863]] `RegulonDB` `C` - regulator=DnaA; target=polA; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-160|complex.ecocyc.MONOMER0-160]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-4565|complex.ecocyc.MONOMER0-4565]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0779|gene.b0779]] `RegulonDB` `C` - regulator=DnaA; target=uvrB; function=-
- `represses` --> [[gene.b1415|gene.b1415]] `RegulonDB` `S` - regulator=DnaA; target=aldA; function=-
- `represses` --> [[gene.b2234|gene.b2234]] `RegulonDB` `C` - regulator=DnaA; target=nrdA; function=-+
- `represses` --> [[gene.b2235|gene.b2235]] `RegulonDB` `C` - regulator=DnaA; target=nrdB; function=-+
- `represses` --> [[gene.b2236|gene.b2236]] `RegulonDB` `C` - regulator=DnaA; target=yfaE; function=-+
- `represses` --> [[gene.b2507|gene.b2507]] `RegulonDB` `S` - regulator=DnaA; target=guaA; function=-
- `represses` --> [[gene.b2508|gene.b2508]] `RegulonDB` `S` - regulator=DnaA; target=guaB; function=-
- `represses` --> [[gene.b3700|gene.b3700]] `RegulonDB` `S` - regulator=DnaA; target=recF; function=-+
- `represses` --> [[gene.b3701|gene.b3701]] `RegulonDB` `C` - regulator=DnaA; target=dnaN; function=-+
- `represses` --> [[gene.b3702|gene.b3702]] `RegulonDB` `S` - regulator=DnaA; target=dnaA; function=-+
- `represses` --> [[gene.b4326|gene.b4326]] `RegulonDB` `C` - regulator=DnaA; target=iraD; function=-
- `represses` --> [[gene.b4670|gene.b4670]] `RegulonDB` `S` - regulator=DnaA; target=yjeV; function=-
- `represses` --> [[gene.b4720|gene.b4720]] `RegulonDB` `C` - regulator=DnaA; target=ytiC; function=-
- `represses` --> [[gene.b4721|gene.b4721]] `RegulonDB` `C` - regulator=DnaA; target=ytiD; function=-
- `represses` --> [[gene.b4722|gene.b4722]] `RegulonDB` `C` - regulator=DnaA; target=idlP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3702|gene.b3702]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03004`
- `KEGG:ecj:JW3679;eco:b3702;`
- `GeneID:93778443;948217;`
- `GO:GO:0003677; GO:0003688; GO:0005524; GO:0005829; GO:0005886; GO:0006260; GO:0006270; GO:0006275; GO:0008289; GO:0009295; GO:0009898; GO:0016787; GO:0030174; GO:0032297; GO:0032298; GO:0042802; GO:0043565; GO:1990078; GO:1990082; GO:1990084; GO:1990101; GO:1990102; GO:1990103`
- `EC:3.6.4.-`

## Notes

Chromosomal replication initiator protein DnaA (EC 3.6.4.-)

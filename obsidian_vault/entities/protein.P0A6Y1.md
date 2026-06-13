---
entity_id: "protein.P0A6Y1"
entity_type: "protein"
name: "ihfB"
source_database: "UniProt"
source_id: "P0A6Y1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ihfB himD hip b0912 JW0895"
---

# ihfB

`protein.P0A6Y1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Y1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: One of the 2 subunits of integration host factor (IHF), a specific DNA-binding protein that functions in genetic recombination as well as in transcriptional and translational control. IHF in combination with the datA locus promotes ATP hydrolysis of ATP-DnaA, called DDAH (datA-dependent DnaA-ATP hydrolysis) (PubMed:23277577). IHF binds oriC as replication initiates, dissociates within minutes and slowly reassociates during the cell cyle; IHF binding to datA is low before initiation, rises after initiation and dissociates during the cell cycle, allowing IHF to coordinate replication initiation (PubMed:23277577). {ECO:0000269|PubMed:23277577}.; FUNCTION: Plays a crucial role in the lysogenic life cycle of bacteriophage lambda, as it is required not only in the recombination reaction, which inserts lambda DNA into the E.coli chromosome, but also for the synthesis of int and cI repressor, two phage proteins necessary for DNA insertion and repression, respectively. The synthesis of int and cI proteins is regulated indirectly by IHF via translational control of the lambda cII protein.; FUNCTION: Has an essential role in conjugative DNA transfer (CDT), the unidirectional transfer of ssDNA plasmid from a donor to a recipient cell. It is the central mechanism by which antibiotic resistance and virulence factors are propagated in bacterial populations...

## Biological Role

Component of DNA-binding transcriptional dual regulator IHF (complex.ecocyc.PC00027).

## Annotation

FUNCTION: One of the 2 subunits of integration host factor (IHF), a specific DNA-binding protein that functions in genetic recombination as well as in transcriptional and translational control. IHF in combination with the datA locus promotes ATP hydrolysis of ATP-DnaA, called DDAH (datA-dependent DnaA-ATP hydrolysis) (PubMed:23277577). IHF binds oriC as replication initiates, dissociates within minutes and slowly reassociates during the cell cyle; IHF binding to datA is low before initiation, rises after initiation and dissociates during the cell cycle, allowing IHF to coordinate replication initiation (PubMed:23277577). {ECO:0000269|PubMed:23277577}.; FUNCTION: Plays a crucial role in the lysogenic life cycle of bacteriophage lambda, as it is required not only in the recombination reaction, which inserts lambda DNA into the E.coli chromosome, but also for the synthesis of int and cI repressor, two phage proteins necessary for DNA insertion and repression, respectively. The synthesis of int and cI proteins is regulated indirectly by IHF via translational control of the lambda cII protein.; FUNCTION: Has an essential role in conjugative DNA transfer (CDT), the unidirectional transfer of ssDNA plasmid from a donor to a recipient cell. It is the central mechanism by which antibiotic resistance and virulence factors are propagated in bacterial populations. Part of the relaxosome, which facilitates a site- and strand-specific cut in the origin of transfer by TraI, at the nic site. Relaxosome formation requires binding of IHF and TraY to the oriT region, which then facilitates binding of TraI (PubMed:7499339, PubMed:7499340). {ECO:0000269|PubMed:7499339, ECO:0000269|PubMed:7499340}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PC00027|complex.ecocyc.PC00027]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0912|gene.b0912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Y1`
- `KEGG:ecj:JW0895;eco:b0912;ecoc:C3026_05620;`
- `GeneID:86945813;93776505;945533;`
- `GO:GO:0003677; GO:0005694; GO:0005829; GO:0006260; GO:0006310; GO:0006351; GO:0006355; GO:0006417; GO:0030527; GO:1990177`

## Notes

Integration host factor subunit beta (IHF-beta)

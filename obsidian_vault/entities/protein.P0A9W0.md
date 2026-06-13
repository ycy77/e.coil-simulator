---
entity_id: "protein.P0A9W0"
entity_type: "protein"
name: "ulaR"
source_database: "UniProt"
source_id: "P0A9W0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaR yjfQ b4191 JW4149"
---

# ulaR

`protein.P0A9W0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9W0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Represses ulaG and the ulaABCDEF operon. Two ulaR binding sites have been identified in each promoter. Full activity requires simultaneous interaction of UlaR with both divergent promoters and seems to be dependent on repressor-mediated DNA loop formation, which is helped by the action of integration host factor. {ECO:0000269|PubMed:12374842, ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:14996803}. UlaR is a DNA-binding transcription factor of 251 amino acids that is expressed constitutively and that coordinately represses transcription of a divergent operon (ula) involved in transport and utilization of L-ascorbate catabolism . Synthesis of these genes is induced when Escherichia coli is grown in the absence of glucose, and under anaerobic conditions it can ferment L-ascorbate; under aerobic conditions it is functional in the presence of casein acid hydrolysate . L-Ascorbate-6-P is the effector of the UlaR transcriptional repressor, and when this small molecule binds to UlaR, it severely impairs the formation of UlaR cognate operator sites, since they form a stable complex . L-Ascorbate-6-P weakens the affinity of UlaR for DNA and displaces the UlaR oligomer state from a transcription-silencing tetrameric form to a transcription-activating dimeric form . UlaR activity is also controlled by homotypic tetramer-dimer transitions regulated by L-ascorbate-6-P...

## Biological Role

Component of UlaR-L-ascorbate-6-phosphate (complex.ecocyc.MONOMER0-2162).

## Annotation

FUNCTION: Represses ulaG and the ulaABCDEF operon. Two ulaR binding sites have been identified in each promoter. Full activity requires simultaneous interaction of UlaR with both divergent promoters and seems to be dependent on repressor-mediated DNA loop formation, which is helped by the action of integration host factor. {ECO:0000269|PubMed:12374842, ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:14996803}.

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2162|complex.ecocyc.MONOMER0-2162]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b4192|gene.b4192]] `RegulonDB` `S` - regulator=UlaR; target=ulaG; function=-
- `represses` --> [[gene.b4193|gene.b4193]] `RegulonDB` `C` - regulator=UlaR; target=ulaA; function=-
- `represses` --> [[gene.b4194|gene.b4194]] `RegulonDB` `C` - regulator=UlaR; target=ulaB; function=-
- `represses` --> [[gene.b4195|gene.b4195]] `RegulonDB` `S` - regulator=UlaR; target=ulaC; function=-
- `represses` --> [[gene.b4196|gene.b4196]] `RegulonDB` `S` - regulator=UlaR; target=ulaD; function=-
- `represses` --> [[gene.b4197|gene.b4197]] `RegulonDB` `S` - regulator=UlaR; target=ulaE; function=-
- `represses` --> [[gene.b4198|gene.b4198]] `RegulonDB` `S` - regulator=UlaR; target=ulaF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4191|gene.b4191]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9W0`
- `KEGG:ecj:JW4149;eco:b4191;ecoc:C3026_22640;`
- `GeneID:75169711;75202425;948706;`
- `GO:GO:0000987; GO:0005737; GO:0006351; GO:0006355; GO:0031418; GO:0045892; GO:0098531`

## Notes

HTH-type transcriptional regulator UlaR

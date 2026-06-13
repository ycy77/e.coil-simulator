---
entity_id: "protein.P37344"
entity_type: "protein"
name: "pspF"
source_database: "UniProt"
source_id: "P37344"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pspF ycjB b1303 JW1296"
---

# pspF

`protein.P37344`

## Static

- Type: `protein`
- Source: `UniProt:P37344`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transcriptional activator for the phage shock protein (psp) operon (pspABCDE) and pspG gene. {ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8606168}. The transcription factor PspF, for "Phage shock protein F," is a bacterial enhancer-binding protein required for RPON-MONOMER σ54-dependent transcription activation . This regulator activates the transcription of the psp regulon, and it is negatively autoregulated and coordinately activated by transcription of the divergent TU00326 operon . The PC00027 "integration host factor" facilitates control of the psp regulon . The psp regulon is defined as the phage shock protein system, which is involved in protecting the bacterium during infectious processes . The synthesis of this regulon is induced when Escherichia coli is grown under different extracytoplasmic stress conditions and upon infection by filamentous phage (phage shock) . The activity of PspF is inhibited by EG10776-MONOMER PspA, which is an accessory protein that binds directly to PspF to inhibit transcription of the psp regulon . PspA inhibits PspF activity by direct interaction of the AAA+ transcription activation domain of PspF . Although PspA appears to regulate transcription of the psp regulon, it does not bind to DNA , but it is necessary for repressing this regulon...

## Biological Role

Component of DNA-binding transcriptional dual regulator PspF (complex.ecocyc.CPLX0-981).

## Annotation

FUNCTION: Transcriptional activator for the phage shock protein (psp) operon (pspABCDE) and pspG gene. {ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8606168}.

## Outgoing Edges (9)

- `activates` --> [[gene.b1304|gene.b1304]] `RegulonDB` `S` - regulator=PspF; target=pspA; function=+
- `activates` --> [[gene.b1305|gene.b1305]] `RegulonDB` `S` - regulator=PspF; target=pspB; function=+
- `activates` --> [[gene.b1306|gene.b1306]] `RegulonDB` `S` - regulator=PspF; target=pspC; function=+
- `activates` --> [[gene.b1307|gene.b1307]] `RegulonDB` `S` - regulator=PspF; target=pspD; function=+
- `activates` --> [[gene.b1308|gene.b1308]] `RegulonDB` `S` - regulator=PspF; target=pspE; function=+
- `activates` --> [[gene.b4050|gene.b4050]] `RegulonDB` `S` - regulator=PspF; target=pspG; function=+
- `activates` --> [[gene.b4758|gene.b4758]] `RegulonDB` `S` - regulator=PspF; target=pspH; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-981|complex.ecocyc.CPLX0-981]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `represses` --> [[gene.b1303|gene.b1303]] `RegulonDB` `S` - regulator=PspF; target=pspF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1303|gene.b1303]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37344`
- `KEGG:ecj:JW1296;eco:b1303;ecoc:C3026_07645;`
- `GeneID:945683;`
- `GO:GO:0000160; GO:0000987; GO:0001216; GO:0003677; GO:0005524; GO:0005667; GO:0005737; GO:0006355; GO:0032993; GO:0042802; GO:0043565; GO:0045892; GO:0045893; GO:0080135`

## Notes

Psp operon transcriptional activator (Phage shock protein F)

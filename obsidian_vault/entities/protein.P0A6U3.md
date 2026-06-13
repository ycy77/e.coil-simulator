---
entity_id: "protein.P0A6U3"
entity_type: "protein"
name: "mnmG"
source_database: "UniProt"
source_id: "P0A6U3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17062623}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mnmG gidA trmF b3741 JW3719"
---

# mnmG

`protein.P0A6U3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6U3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17062623}.

## Enriched Summary

FUNCTION: NAD-binding protein involved in the addition of a carboxymethylaminomethyl (cmnm) group at the wobble position (U34) of certain tRNAs, forming tRNA-cmnm(5)s(2)U34. {ECO:0000269|PubMed:11544186, ECO:0000269|PubMed:17062623, ECO:0000269|PubMed:9603884}. MnmG is required for wild-type 5-methylaminomethyl-2-thiouridine modification of tRNA . The additional modification of m5U stabilizes the U·G pairing at the wobble position and thus plays a role in decoding NNG codons . MnmG and MnmE both act in a tRNA modification pathway that reduces +2 frameshift errors in translation . Transcription of mnmG, which is adjacent to oriC, appeared to affect DNA replication . Subsequently it was shown that transcription of mnmG is only required for oriC activation under suboptimal conditions . However, MnmG does appear to promote cell division . The MnmG protein is a dimer in solution, interacts specifically with MnmE, and binds FAD. Mutations in the conserved G13 and G15 residues of the proposed FAD binding site lead to loss of FAD binding and loss of methylaminomethyl modification of tRNAs . Crystal structures of MnmG have been solved , showing the location of the FAD binding site and the dimerization interface, as well as suggesting sites for the interaction with tRNA . The C-terminal domain is required for the interaction with MnmE...

## Biological Role

Component of 5-carboxymethylaminomethyluridine-tRNA synthase subunit MnmG (complex.ecocyc.CPLX0-7597), 5-carboxymethylaminomethyluridine-tRNA synthase [multifunctional] (complex.ecocyc.CPLX0-7609).

## Annotation

FUNCTION: NAD-binding protein involved in the addition of a carboxymethylaminomethyl (cmnm) group at the wobble position (U34) of certain tRNAs, forming tRNA-cmnm(5)s(2)U34. {ECO:0000269|PubMed:11544186, ECO:0000269|PubMed:17062623, ECO:0000269|PubMed:9603884}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7597|complex.ecocyc.CPLX0-7597]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7609|complex.ecocyc.CPLX0-7609]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3741|gene.b3741]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6U3`
- `KEGG:ecj:JW3719;eco:b3741;ecoc:C3026_20270;`
- `GeneID:75173975;75205459;948248;`
- `GO:GO:0002098; GO:0002144; GO:0002926; GO:0005829; GO:0009411; GO:0030488; GO:0042803; GO:0050660; GO:0140018`

## Notes

tRNA uridine 5-carboxymethylaminomethyl modification enzyme MnmG (Glucose-inhibited division protein A)

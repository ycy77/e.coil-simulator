---
entity_id: "protein.P33224"
entity_type: "protein"
name: "aidB"
source_database: "UniProt"
source_id: "P33224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aidB b4187 JW5867"
---

# aidB

`protein.P33224`

## Static

- Type: `protein`
- Source: `UniProt:P33224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the adaptive DNA-repair response to alkylating agents. Could prevent alkylation damage by protecting DNA and destroying alkylating agents that have yet to reach their DNA target. Binds to double-stranded DNA with a preference for a DNA region that includes its own promoter. Shows weak isovaleryl-CoA dehydrogenase activity in vitro. {ECO:0000269|PubMed:16352838, ECO:0000269|PubMed:18829440, ECO:0000269|PubMed:7961409}. AidB is a multifunctional protein that forms part of E.coli's adaptive response to alkylating agents as defined by the ada regulon. The biological role of AidB is not clear - the purified protein has low levels of isovaleryl-CoA dehydrogenase activity, displays DNA binding activity and can negatively regulate its own expression in vivo. Apo AidB has a high affinity for flavin adenine dinucleotide (FAD), which helps with the assembly of the AidB tetramer . AidB was overexpressed, purified, and found to contain a FAD cofactor in stoichiometric quantities . The purified protein has a very low level of isovaleryl-CoA dehydrogenase activity and binds double-stranded DNA with a preference for methylated and/or relaxed DNA . In in vitro binding experiments AidB shows preferential binding to a DNA region that includes the upstream sequence and -35 box of its own promoter . AidB can repress its own synthesis during normal cell growth...

## Biological Role

Component of isovaleryl-CoA dehydrogenase and DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7691).

## Annotation

FUNCTION: Part of the adaptive DNA-repair response to alkylating agents. Could prevent alkylation damage by protecting DNA and destroying alkylating agents that have yet to reach their DNA target. Binds to double-stranded DNA with a preference for a DNA region that includes its own promoter. Shows weak isovaleryl-CoA dehydrogenase activity in vitro. {ECO:0000269|PubMed:16352838, ECO:0000269|PubMed:18829440, ECO:0000269|PubMed:7961409}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7691|complex.ecocyc.CPLX0-7691]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b4187|gene.b4187]] `RegulonDB` `S` - regulator=AidB; target=aidB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4187|gene.b4187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33224`
- `KEGG:ecj:JW5867;eco:b4187;ecoc:C3026_22620;`
- `GeneID:948710;`
- `GO:GO:0003677; GO:0003995; GO:0005737; GO:0006974; GO:0008470; GO:0042802; GO:0043565; GO:0045892`
- `EC:1.3.99.-`

## Notes

Putative acyl-CoA dehydrogenase AidB (EC 1.3.99.-)

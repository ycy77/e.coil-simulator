---
entity_id: "protein.P77309"
entity_type: "protein"
name: "yneJ"
source_database: "UniProt"
source_id: "P77309"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yneJ b1526 JW1519"
---

# yneJ

`protein.P77309`

## Static

- Type: `protein`
- Source: `UniProt:P77309`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YneJ The LysR-type transcriptional regulator PtrR, putrescine utilization regulator, is involved in L-glutamate and putrescine metabolism and in resistance to the tetracycline group of antibiotics . Additionally, was predicted to regulate genes related to iron and succinate oxidation . PtrR contains a helix-turn-helix motif for DNA binding in its N-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like PtrR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The efficiency of PtrR binding to DNA was found to be more robust in the presence of Gln than Glu or putrescine . Genome-wide PtrR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and by ChIP-seq in M9 minimal medium with putrescine and with tryptone . The transcriptional response to the deletion of PtrR was characterized by RNA-seq in M9 minimal medium with Ptr and/or Glu as nitrogen source . By the integrative analysis of ChIP-exo and RNA-seq data, it was determined that PtrR directly represses the transcription of the sad gene (encoding the succinate-semialdehyde dehydrogenase) and probably fnrS]|...

## Biological Role

Component of PtrR-glt (complex.ecocyc.CPLX0-10427), DNA-binding transcriptional regulator PtrR-L-glutamine (complex.ecocyc.CPLX0-10428), PtrR-4-aminobutanoate (complex.ecocyc.CPLX0-9318).

## Annotation

Uncharacterized HTH-type transcriptional regulator YneJ

## Outgoing Edges (7)

- `activates` --> [[gene.b1523|gene.b1523]] `RegulonDB` `S` - regulator=PtrR; target=yneG; function=+
- `activates` --> [[gene.b1524|gene.b1524]] `RegulonDB` `S` - regulator=PtrR; target=glsB; function=+
- `activates` --> [[gene.b1525|gene.b1525]] `RegulonDB` `S` - regulator=PtrR; target=sad; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-10427|complex.ecocyc.CPLX0-10427]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9318|complex.ecocyc.CPLX0-9318]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0464|gene.b0464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1526|gene.b1526]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77309`
- `KEGG:ecj:JW1519;eco:b1526;ecoc:C3026_08820;`
- `GeneID:946079;`
- `GO:GO:0000976; GO:0003700; GO:0006355`

## Notes

Uncharacterized HTH-type transcriptional regulator YneJ

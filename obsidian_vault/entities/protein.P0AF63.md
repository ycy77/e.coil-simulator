---
entity_id: "protein.P0AF63"
entity_type: "protein"
name: "nsrR"
source_database: "UniProt"
source_id: "P0AF63"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nsrR yjeB b4178 JW4136"
---

# nsrR

`protein.P0AF63`

## Static

- Type: `protein`
- Source: `UniProt:P0AF63`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Nitric oxide-sensitive repressor of genes involved in protecting the cell against nitrosative stress, such as ytfE, hmpA and ygbA. May require iron for activity. Does not regulate its own transcription. {ECO:0000269|PubMed:16428390}.

## Biological Role

Component of NsrR-nitric oxide (complex.ecocyc.CPLX0-7751), DNA-binding transcriptional dual regulator NsrR (complex.ecocyc.CPLX0-7756).

## Annotation

FUNCTION: Nitric oxide-sensitive repressor of genes involved in protecting the cell against nitrosative stress, such as ytfE, hmpA and ygbA. May require iron for activity. Does not regulate its own transcription. {ECO:0000269|PubMed:16428390}.

## Outgoing Edges (12)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7751|complex.ecocyc.CPLX0-7751]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7756|complex.ecocyc.CPLX0-7756]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0871|gene.b0871]] `RegulonDB` `C` - regulator=NsrR; target=poxB; function=-
- `represses` --> [[gene.b0872|gene.b0872]] `RegulonDB` `C` - regulator=NsrR; target=hcr; function=-
- `represses` --> [[gene.b0873|gene.b0873]] `RegulonDB` `C` - regulator=NsrR; target=hcp; function=-
- `represses` --> [[gene.b1920|gene.b1920]] `RegulonDB` `S` - regulator=NsrR; target=tcyJ; function=-
- `represses` --> [[gene.b4071|gene.b4071]] `RegulonDB` `C` - regulator=NsrR; target=nrfB; function=-
- `represses` --> [[gene.b4072|gene.b4072]] `RegulonDB` `C` - regulator=NsrR; target=nrfC; function=-
- `represses` --> [[gene.b4073|gene.b4073]] `RegulonDB` `C` - regulator=NsrR; target=nrfD; function=-
- `represses` --> [[gene.b4074|gene.b4074]] `RegulonDB` `C` - regulator=NsrR; target=nrfE; function=-
- `represses` --> [[gene.b4075|gene.b4075]] `RegulonDB` `C` - regulator=NsrR; target=nrfF; function=-
- `represses` --> [[gene.b4209|gene.b4209]] `RegulonDB` `S` - regulator=NsrR; target=ytfE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4178|gene.b4178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF63`
- `KEGG:ecj:JW4136;eco:b4178;ecoc:C3026_22575;`
- `GeneID:86861428;93777643;948693;`
- `GO:GO:0003690; GO:0003700; GO:0005506; GO:0005829; GO:0006355; GO:0045892; GO:0051537`

## Notes

HTH-type transcriptional repressor NsrR

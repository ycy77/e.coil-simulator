---
entity_id: "protein.P0A8S1"
entity_type: "protein"
name: "argP"
source_database: "UniProt"
source_id: "P0A8S1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argP iciA b2916 JW2883"
---

# argP

`protein.P0A8S1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8S1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Controls the transcription of genes involved in arginine and lysine metabolism. Activates transcription of several genes, including argO, lysP, lysC, asd, dapB, dapD, lysA, gdhA and argK. Acts by binding directly to their promoter or control region (PubMed:10600368, PubMed:15150242, PubMed:17504942, PubMed:21441513, PubMed:21890697). ArgP dimer by itself is able to bind the argO promoter-operator region to form a binary complex, but the formation of a ternary complex with RNA polymerase is greatly stimulated only in presence of a coeffector. Both arginine and lysine are coeffectors at the argO promoter, but only arginine is competent to activate transcription. Lysine has repressive effects (PubMed:15150242, PubMed:17504942). ArgP also mediates lysine repression of dapB, and gdhA in vivo, but via an alternative mechanism: ArgP binding is directly reduced upon the addition of lysine (PubMed:21890697). Binds in vitro to the promoter region of dnaA and to the upstream region of the nrd promoter, but these genes are probably not regulated by ArgP in vivo (PubMed:21890697, PubMed:9254708, PubMed:9819053). In vitro, also binds to the three 13-mers located in the origin region (oriC) and blocks the initiation of replication (PubMed:1733927)...

## Biological Role

Component of DNA-binding transcriptional dual regulator ArgP (complex.ecocyc.CPLX0-7669).

## Annotation

FUNCTION: Controls the transcription of genes involved in arginine and lysine metabolism. Activates transcription of several genes, including argO, lysP, lysC, asd, dapB, dapD, lysA, gdhA and argK. Acts by binding directly to their promoter or control region (PubMed:10600368, PubMed:15150242, PubMed:17504942, PubMed:21441513, PubMed:21890697). ArgP dimer by itself is able to bind the argO promoter-operator region to form a binary complex, but the formation of a ternary complex with RNA polymerase is greatly stimulated only in presence of a coeffector. Both arginine and lysine are coeffectors at the argO promoter, but only arginine is competent to activate transcription. Lysine has repressive effects (PubMed:15150242, PubMed:17504942). ArgP also mediates lysine repression of dapB, and gdhA in vivo, but via an alternative mechanism: ArgP binding is directly reduced upon the addition of lysine (PubMed:21890697). Binds in vitro to the promoter region of dnaA and to the upstream region of the nrd promoter, but these genes are probably not regulated by ArgP in vivo (PubMed:21890697, PubMed:9254708, PubMed:9819053). In vitro, also binds to the three 13-mers located in the origin region (oriC) and blocks the initiation of replication (PubMed:1733927). {ECO:0000269|PubMed:10600368, ECO:0000269|PubMed:15150242, ECO:0000269|PubMed:1733927, ECO:0000269|PubMed:17504942, ECO:0000269|PubMed:21441513, ECO:0000269|PubMed:21890697, ECO:0000269|PubMed:9254708, ECO:0000269|PubMed:9819053}.

## Outgoing Edges (15)

- `activates` --> [[gene.b0031|gene.b0031]] `RegulonDB` `C` - regulator=ArgP; target=dapB; function=+
- `activates` --> [[gene.b0166|gene.b0166]] `RegulonDB` `S` - regulator=ArgP; target=dapD; function=+
- `activates` --> [[gene.b1761|gene.b1761]] `RegulonDB` `C` - regulator=ArgP; target=gdhA; function=+
- `activates` --> [[gene.b2156|gene.b2156]] `RegulonDB` `C` - regulator=ArgP; target=lysP; function=+
- `activates` --> [[gene.b2234|gene.b2234]] `RegulonDB` `S` - regulator=ArgP; target=nrdA; function=+
- `activates` --> [[gene.b2235|gene.b2235]] `RegulonDB` `S` - regulator=ArgP; target=nrdB; function=+
- `activates` --> [[gene.b2236|gene.b2236]] `RegulonDB` `S` - regulator=ArgP; target=yfaE; function=+
- `activates` --> [[gene.b2838|gene.b2838]] `RegulonDB` `S` - regulator=ArgP; target=lysA; function=+
- `activates` --> [[gene.b2923|gene.b2923]] `RegulonDB` `C` - regulator=ArgP; target=argO; function=+
- `activates` --> [[gene.b3433|gene.b3433]] `RegulonDB` `S` - regulator=ArgP; target=asd; function=+
- `activates` --> [[gene.b3700|gene.b3700]] `RegulonDB` `S` - regulator=ArgP; target=recF; function=+
- `activates` --> [[gene.b3701|gene.b3701]] `RegulonDB` `S` - regulator=ArgP; target=dnaN; function=+
- `activates` --> [[gene.b3702|gene.b3702]] `RegulonDB` `S` - regulator=ArgP; target=dnaA; function=+
- `activates` --> [[gene.b4024|gene.b4024]] `RegulonDB` `S` - regulator=ArgP; target=lysC; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7669|complex.ecocyc.CPLX0-7669]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2916|gene.b2916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8S1`
- `KEGG:ecj:JW2883;eco:b2916;ecoc:C3026_15980;`
- `GeneID:93779084;944867;`
- `GO:GO:0003681; GO:0003700; GO:0006355; GO:0032297; GO:0043565; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulator ArgP (Inhibitor of chromosome initiation) (OriC replication inhibitor)

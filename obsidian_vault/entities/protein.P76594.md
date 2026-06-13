---
entity_id: "protein.P76594"
entity_type: "protein"
name: "patZ"
source_database: "UniProt"
source_id: "P76594"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "patZ pka yfiQ b2584 JW2568"
---

# patZ

`protein.P76594`

## Static

- Type: `protein`
- Source: `UniProt:P76594`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the acetyl-CoA-dependent acetylation of lysine residues of a large number of target proteins. Acetylates RNase R in exponential phase cells and RNase II (PubMed:21981926, PubMed:22124017, PubMed:26847092). Required for the glucose-dependent acetylation on multiple lysines of alpha, beta and beta' RNAP subunits (PubMed:21696463). Also acetylates acetyl-coenzyme A synthetase (Acs) and the chromosomal replication initiator protein DnaA, and inhibits their activity (PubMed:22059728, PubMed:26251518, PubMed:27484197). Overexpression leads to the acetylation of a large number of additional proteins and inhibits motility (PubMed:30352934). {ECO:0000269|PubMed:21696463, ECO:0000269|PubMed:21981926, ECO:0000269|PubMed:22059728, ECO:0000269|PubMed:22124017, ECO:0000269|PubMed:26251518, ECO:0000269|PubMed:26847092, ECO:0000269|PubMed:27484197, ECO:0000269|PubMed:30352934}.

## Biological Role

Component of peptidyl-lysine N-acetyltransferase (complex.ecocyc.CPLX0-8189).

## Annotation

FUNCTION: Catalyzes the acetyl-CoA-dependent acetylation of lysine residues of a large number of target proteins. Acetylates RNase R in exponential phase cells and RNase II (PubMed:21981926, PubMed:22124017, PubMed:26847092). Required for the glucose-dependent acetylation on multiple lysines of alpha, beta and beta' RNAP subunits (PubMed:21696463). Also acetylates acetyl-coenzyme A synthetase (Acs) and the chromosomal replication initiator protein DnaA, and inhibits their activity (PubMed:22059728, PubMed:26251518, PubMed:27484197). Overexpression leads to the acetylation of a large number of additional proteins and inhibits motility (PubMed:30352934). {ECO:0000269|PubMed:21696463, ECO:0000269|PubMed:21981926, ECO:0000269|PubMed:22059728, ECO:0000269|PubMed:22124017, ECO:0000269|PubMed:26251518, ECO:0000269|PubMed:26847092, ECO:0000269|PubMed:27484197, ECO:0000269|PubMed:30352934}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8189|complex.ecocyc.CPLX0-8189]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2584|gene.b2584]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76594`
- `KEGG:ecj:JW2568;eco:b2584;ecoc:C3026_14320;`
- `GeneID:947056;`
- `GO:GO:0005524; GO:0006979; GO:0009408; GO:0032991; GO:0042802; GO:0046872; GO:0061733`
- `EC:2.3.1.-`

## Notes

Peptidyl-lysine N-acetyltransferase PatZ (EC 2.3.1.-) (Protein lysine acetyltransferase)

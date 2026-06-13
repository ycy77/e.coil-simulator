---
entity_id: "protein.P0A968"
entity_type: "protein"
name: "cspD"
source_database: "UniProt"
source_id: "P0A968"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cspD cspH ybjA b0880 JW0864"
---

# cspD

`protein.P0A968`

## Static

- Type: `protein`
- Source: `UniProt:P0A968`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Inhibits DNA replication at both initiation and elongation steps, most probably by binding to the opened, single-stranded regions at replication forks. Plays a regulatory role in chromosomal replication in nutrient-depleted cells.; FUNCTION: Involved in persister cell formation, acting downstream of mRNA interferase (toxin) MqsR. Overproduction is toxic. CspD is a toxin that appears to act by inhibiting replication , and which influences persister cell formation . CspD forms a homodimer in solution, is able to bind single-stranded DNA and RNA, and packs ssDNA into structures that are distinguishable from SSB-coated DNA. Binding does not show sequence specificity. In vitro, CspD inhibits initiation and elongation of minichromosome replication . The CspD protein localizes to the nucleoid in stationary-phase cells . Expression of cspD is not inducible by cold shock and is inversely correlated with growth rate; it is induced at stationary phase and upon glucose starvation, but is not dependent on σS, the stationary phase sigma factor . Expression is upregulated by the golbal metabolic regulator CRP . showed cspD to be highly expressed at all time points including long-term stationary phase...

## Biological Role

Component of DNA replication inhibitor CspD (complex.ecocyc.CPLX0-3301).

## Annotation

FUNCTION: Inhibits DNA replication at both initiation and elongation steps, most probably by binding to the opened, single-stranded regions at replication forks. Plays a regulatory role in chromosomal replication in nutrient-depleted cells.; FUNCTION: Involved in persister cell formation, acting downstream of mRNA interferase (toxin) MqsR. Overproduction is toxic.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3301|complex.ecocyc.CPLX0-3301]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0880|gene.b0880]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A968`
- `KEGG:ecj:JW0864;eco:b0880;ecoc:C3026_05465;`
- `GeneID:86863395;93776540;945669;`
- `GO:GO:0003676; GO:0003697; GO:0003723; GO:0005829; GO:0006355; GO:0008156; GO:0010468; GO:0042594; GO:0042803; GO:0090729`

## Notes

Cold shock-like protein CspD (CSP-D)

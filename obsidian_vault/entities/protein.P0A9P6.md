---
entity_id: "protein.P0A9P6"
entity_type: "protein"
name: "deaD"
source_database: "UniProt"
source_id: "P0A9P6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00964, ECO:0000269|PubMed:8552679}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deaD csdA mssB rhlD b3162 JW5531"
---

# deaD

`protein.P0A9P6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9P6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00964, ECO:0000269|PubMed:8552679}.

## Enriched Summary

FUNCTION: DEAD-box RNA helicase involved in various cellular processes at low temperature, including ribosome biogenesis, mRNA degradation and translation initiation. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity at low temperature. Involved in 50S ribosomal subunit assembly, acting after SrmB, and could also play a role in the biogenesis of the 30S ribosomal subunit. In addition, is involved in mRNA decay, via formation of a cold-shock degradosome with RNase E. Also stimulates translation of some mRNAs, probably at the level of initiation. {ECO:0000255|HAMAP-Rule:MF_00964, ECO:0000269|PubMed:10216955, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:15554978, ECO:0000269|PubMed:17259309, ECO:0000269|PubMed:8552679}.

## Biological Role

Component of ATP-dependent RNA helicase DeaD (complex.ecocyc.CPLX0-8557).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: DEAD-box RNA helicase involved in various cellular processes at low temperature, including ribosome biogenesis, mRNA degradation and translation initiation. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity at low temperature. Involved in 50S ribosomal subunit assembly, acting after SrmB, and could also play a role in the biogenesis of the 30S ribosomal subunit. In addition, is involved in mRNA decay, via formation of a cold-shock degradosome with RNase E. Also stimulates translation of some mRNAs, probably at the level of initiation. {ECO:0000255|HAMAP-Rule:MF_00964, ECO:0000269|PubMed:10216955, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:15554978, ECO:0000269|PubMed:17259309, ECO:0000269|PubMed:8552679}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (2)

- `activates` --> [[gene.b0925|gene.b0925]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `is_component_of` --> [[complex.ecocyc.CPLX0-8557|complex.ecocyc.CPLX0-8557]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3162|gene.b3162]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9P6`
- `KEGG:ecj:JW5531;eco:b3162;ecoc:C3026_17225;`
- `GeneID:93778822;947674;`
- `GO:GO:0000027; GO:0003724; GO:0005524; GO:0005829; GO:0006401; GO:0009314; GO:0009409; GO:0016887; GO:0033592; GO:0042803; GO:0045727; GO:0048255; GO:0070417`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock DEAD box protein A) (Translation factor W2)

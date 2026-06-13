---
entity_id: "protein.P21893"
entity_type: "protein"
name: "recJ"
source_database: "UniProt"
source_id: "P21893"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recJ b2892 JW2860"
---

# recJ

`protein.P21893`

## Static

- Type: `protein`
- Source: `UniProt:P21893`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Single-stranded-DNA-specific exonuclease. Required for many types of recombinational events, although the stringency of the requirement for RecJ appears to vary with the type of recombinational event monitored and the other recombination gene products which are available. {ECO:0000269|PubMed:2649886}. RecJ is a ssDNA-specific processive exonuclease that is involved in recombination and RecF-dependent repair . RecJ belongs to the RecF epistatic group of DNA recombination/repair genes . The early steps of dsDNA break repair have been reconstituted in vitro using purified components of the RecF recombinational repair system . RecJ only acts on ssDNA. Efficient binding requires a single-stranded 5' tail of at least 7 nucleotides; a 5' phosphate group is not required. Only one RecJ molecule binds per substrate molecule. Prebinding of ssDNA by SSB enhances RecJ activity . RecJ and the RecQ helicase functionally interact in double-strand break repair . At blocked replication forks, RecJ and RecQ process the nascent lagging strand DNA, enabling stabilization of the replication fork until the DNA damage is repaired . RecJ is required for the recovery of DNA synthesis after replication arrest . However, in recF, recR or recA mutants, the nascent DNA at the replication fork is degraded due to the RecQ helicase and RecJ nuclease activities...

## Biological Role

Catalyzes 3.1.11.6-RXN (reaction.ecocyc.3.1.11.6-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Single-stranded-DNA-specific exonuclease. Required for many types of recombinational events, although the stringency of the requirement for RecJ appears to vary with the type of recombinational event monitored and the other recombination gene products which are available. {ECO:0000269|PubMed:2649886}.

## Pathways

- `eco03410` Base excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.11.6-RXN|reaction.ecocyc.3.1.11.6-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2892|gene.b2892]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21893`
- `KEGG:ecj:JW2860;eco:b2892;ecoc:C3026_15860;`
- `GeneID:947367;`
- `GO:GO:0003676; GO:0006281; GO:0006310; GO:0010165; GO:0045145`
- `EC:3.1.-.-`

## Notes

Single-stranded-DNA-specific exonuclease RecJ (EC 3.1.-.-)

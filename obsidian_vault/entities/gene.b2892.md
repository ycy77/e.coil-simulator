---
entity_id: "gene.b2892"
entity_type: "gene"
name: "recJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2892"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2892"
  - "recJ"
---

# recJ

`gene.b2892`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2892`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recJ (gene.b2892) is a gene entity. It encodes recJ (protein.P21893). Encoded protein function: FUNCTION: Single-stranded-DNA-specific exonuclease. Required for many types of recombinational events, although the stringency of the requirement for RecJ appears to vary with the type of recombinational event monitored and the other recombination gene products which are available. {ECO:0000269|PubMed:2649886}. EcoCyc product frame: EG10830-MONOMER. Genomic coordinates: 3036373-3038106. EcoCyc protein note: RecJ is a ssDNA-specific processive exonuclease that is involved in recombination and RecF-dependent repair . RecJ belongs to the RecF epistatic group of DNA recombination/repair genes . The early steps of dsDNA break repair have been reconstituted in vitro using purified components of the RecF recombinational repair system . RecJ only acts on ssDNA. Efficient binding requires a single-stranded 5' tail of at least 7 nucleotides; a 5' phosphate group is not required. Only one RecJ molecule binds per substrate molecule. Prebinding of ssDNA by SSB enhances RecJ activity . RecJ and the RecQ helicase functionally interact in double-strand break repair . At blocked replication forks, RecJ and RecQ process the nascent lagging strand DNA, enabling stabilization of the replication fork until the DNA damage is repaired...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21893|protein.P21893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=recJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009492,ECOCYC:EG10830,GeneID:947367`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3036373-3038106:-; feature_type=gene

---
entity_id: "gene.b2324"
entity_type: "gene"
name: "mnmC"
source_database: "NCBI RefSeq"
source_id: "gene-b2324"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2324"
  - "mnmC"
---

# mnmC

`gene.b2324`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2324`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mnmC (gene.b2324) is a gene entity. It encodes mnmC (protein.P77182). Encoded protein function: FUNCTION: Catalyzes the last two steps in the biosynthesis of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at the wobble position (U34) in tRNA. Catalyzes the FAD-dependent demodification of cmnm(5)s(2)U34 to nm(5)s(2)U34, followed by the transfer of a methyl group from S-adenosyl-L-methionine to nm(5)s(2)U34, to form mnm(5)s(2)U34. {ECO:0000269|PubMed:15247431, ECO:0000269|PubMed:18186482}. EcoCyc product frame: G7199-MONOMER. EcoCyc synonyms: yfcK, trmC. Genomic coordinates: 2441764-2443770. EcoCyc protein note: The tRNAs specific for glutamate, lysine, and possibly glutamine contain the hypermodified nucleoside 5-methylaminomethyl-2-thiouridine (mnm5s2U) in position 34, the wobble position. The MnmC protein was shown to catalyze the formation of mnm5s2U from 5-carboxymethylaminomethyl-2-thiouridine (cmnm5s2U) in tRNA . Both the tRNA species and growth conditions modulate synthesis of the wobble base modifications . A tentative reaction mechanism has been proposed. The enzyme catalyzes two steps, an initial FAD-dependent demodification of cmnm5s2U to nm5s2U followed by the transfer of a methyl group from AdoMet to nm5s2U to produce mnm5s2U...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77182|protein.P77182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007681,ECOCYC:G7199,GeneID:946800`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2441764-2443770:+; feature_type=gene

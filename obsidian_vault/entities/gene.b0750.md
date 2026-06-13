---
entity_id: "gene.b0750"
entity_type: "gene"
name: "nadA"
source_database: "NCBI RefSeq"
source_id: "gene-b0750"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0750"
  - "nadA"
---

# nadA

`gene.b0750`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0750`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadA (gene.b0750) is a gene entity. It encodes nadA (protein.P11458). Encoded protein function: FUNCTION: Catalyzes the condensation of iminoaspartate with dihydroxyacetone phosphate to form quinolinate. {ECO:0000255|HAMAP-Rule:MF_00567, ECO:0000269|PubMed:10648170, ECO:0000269|PubMed:15898769, ECO:0000269|PubMed:15967443, ECO:0000269|PubMed:18674537}. EcoCyc product frame: QUINOLINATE-SYNTHA-MONOMER. EcoCyc synonyms: nicA. Genomic coordinates: 782085-783128. EcoCyc protein note: Quinolinate synthase catalyzes the second reaction in the de novo biosynthesis of NAD from aspartate, the condensation of IMINOASPARTATE with DIHYDROXY-ACETONE-PHOSPHATE to form QUINOLINATE. NadA was shown to contain an oxygen-sensitive [4Fe-4S] cluster that is required for its activity , explaining the NAD auxotrophy of an G7325 mutant. Reaction mechanisms involving the [4Fe-4S] cluster have been proposed . The conserved C113, C200 and C297 residues are involved in [4Fe-4S] cluster binding . The C291 and C294 residues appear to undergo reversible disulfide bond formation that regulates the activity of the enzyme . The midpoint potential of -264 mV is similar to that of thioredoxin and of the cytosol . Overexpression of NadA of E...

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11458|protein.P11458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002541,ECOCYC:EG10630,GeneID:945351`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:782085-783128:+; feature_type=gene

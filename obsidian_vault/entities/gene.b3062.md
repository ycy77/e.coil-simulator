---
entity_id: "gene.b3062"
entity_type: "gene"
name: "ttdB"
source_database: "NCBI RefSeq"
source_id: "gene-b3062"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3062"
  - "ttdB"
---

# ttdB

`gene.b3062`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3062`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ttdB (gene.b3062) is a gene entity. It encodes ttdB (protein.P0AC35). Encoded protein function: L(+)-tartrate dehydratase subunit beta (L-TTD beta) (EC 4.2.1.32) EcoCyc product frame: TTDB-MONOMER. EcoCyc synonyms: ygjB. Genomic coordinates: 3207371-3207976. EcoCyc protein note: The ttdB gene encodes the β subunit of L-tartrate dehydratase . Expression may be translationally coupled to TtdA . ttdB shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A ttdB deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses . TtdB: "L-tartrate dehydratase B"

## Biological Role

Activated by ttdR (protein.P45463).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC35|protein.P0AC35]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P45463|protein.P45463]] `RegulonDB` `S` - regulator=Dan; target=ttdB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010052,ECOCYC:EG11169,GeneID:947568`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3207371-3207976:+; feature_type=gene

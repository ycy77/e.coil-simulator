---
entity_id: "gene.b0178"
entity_type: "gene"
name: "skp"
source_database: "NCBI RefSeq"
source_id: "gene-b0178"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0178"
  - "skp"
---

# skp

`gene.b0178`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0178`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

skp (gene.b0178) is a gene entity. It encodes skp (protein.P0AEU7). Encoded protein function: FUNCTION: Molecular chaperone that interacts specifically with outer membrane proteins, thus maintaining the solubility of early folding intermediates during passage through the periplasm. Required for the efficient release of OmpA from the inner membrane, the maintenance of its solubility in the periplasm, and, in association with lipopolysaccharide (LPS), for the efficient folding and insertion of OmpA into the outer membrane. {ECO:0000269|PubMed:10455120, ECO:0000269|PubMed:11278858, ECO:0000269|PubMed:12509434, ECO:0000269|PubMed:8730870, ECO:0000269|PubMed:9914480}. EcoCyc product frame: EG10455-MONOMER. EcoCyc synonyms: ompH, hlpA, firA. Genomic coordinates: 200482-200967. EcoCyc protein note: Skp is a periplasmic chaperone which functions during the biogenesis of outer membrane proteins (OMPs). Skp prevents folding of EG10669-MONOMER OmpA in solution; Skp and lipopolysaccharide (LPS) improve insertion of OmpA into phospholipid bilayers . Skp prevents EG12180-MONOMER PagP aggregation in vitro and accelerates PagP folding into negatively charged liposomes . Skp interacts with OmpA and PhoE in close proximity to the inner membrane; Skp interacts with early folding intermediates of outer membrane proteins...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEU7|protein.P0AEU7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=skp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000608,ECOCYC:EG10455,GeneID:944861`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:200482-200967:+; feature_type=gene

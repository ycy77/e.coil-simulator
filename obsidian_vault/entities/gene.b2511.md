---
entity_id: "gene.b2511"
entity_type: "gene"
name: "der"
source_database: "NCBI RefSeq"
source_id: "gene-b2511"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2511"
  - "der"
---

# der

`gene.b2511`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2511`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

der (gene.b2511) is a gene entity. It encodes der (protein.P0A6P5). Encoded protein function: FUNCTION: GTPase that plays an essential role in the late steps of ribosome biogenesis. GTPase point mutations (but not a deletion mutant) are suppressed by mild overexpression of RelA, probably due to increased levels of the stringent response mediator (p)ppGpp. 50S subunits assembled in the absence of Der are defective and unable to assemble into 70S ribosomes. GTPase activity is stimulated by YihI. Overexpression rescues an rrmJ deletion, stabilizing the 70S ribosome. Der and RrmJ are likely to share a mechanism to stabilize 50S ribosomal subunits at a very late stage of 50S subunit maturation possibly by interacting with 23S rRNA or 23S rRNA/r-protein complex. {ECO:0000269|PubMed:11976298, ECO:0000269|PubMed:16930151}. EcoCyc product frame: G7319-MONOMER. EcoCyc synonyms: engA, yfgK. Genomic coordinates: 2635884-2637356. EcoCyc protein note: The Der protein is a GTPase that is ubiquitously conserved in eubacteria . It is associated with the large ribosomal subunit and is required for its stability . In E. coli, Der is essential for growth . GTP hydrolysis appears to regulate the specificity of interactions of Der with ribosomal subunits . The GAP-like protein CPLX0-7853 "YihI" interacts with Der and activates its GTPase activity...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6P5|protein.P0A6P5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=der; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008270,ECOCYC:G7319,GeneID:946983`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2635884-2637356:-; feature_type=gene

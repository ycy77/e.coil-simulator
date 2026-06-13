---
entity_id: "gene.b1024"
entity_type: "gene"
name: "pgaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1024"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1024"
  - "pgaA"
---

# pgaA

`gene.b1024`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1024`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgaA (gene.b1024) is a gene entity. It encodes pgaA (protein.P69434). Encoded protein function: FUNCTION: Exports the biofilm adhesin polysaccharide poly-beta-1,6-N-acetyl-D-glucosamine (PGA) across the outer membrane. The PGA transported seems to be partially N-deacetylated since N-deacetylation of PGA by PgaB is needed for PGA export through the PgaA porin.; FUNCTION: Required for the synthesis of the beta-1,6-GlcNAc polysaccharide (PGA or poly-GlcNAc) that seems to serve as a biofilm adhesin. EcoCyc product frame: G6531-MONOMER. EcoCyc synonyms: hmsH, ycdS. Genomic coordinates: 1089866-1092289. EcoCyc protein note: The pgaABCD locus is required for the synthesis of a cell-bound hexosamine-rich polysaccharide, which was identified as a linear polymer of β-1,6-N-acetylglucosamine residues (PGA), an adhesin essential in biofilm formation . PgaA exports PGA across the outer membrane. N-deacetylation of PGA by PgaB promotes its transport across the outer membrane. A pgaA mutant has reduced biofilm formation . pgaA mutants do not release significant amounts of PGA into the medium during shaking compared to wild-type . PGA from pgaA mutants is not externally exposed, showing PgaA is involved in transport of PGA across the outer membrane . Expression of pgaABCD is higher at 37°C than at 21°C and is highest during stationary phase...

## Biological Role

Repressed by ompR (protein.P0AA16), csrA (protein.P69913). Activated by nhaR (protein.P0A9G2), nac (protein.Q47005).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69434|protein.P69434]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=pgaA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pgaA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=pgaA; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003469,ECOCYC:G6531,GeneID:945596`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1089866-1092289:-; feature_type=gene

---
entity_id: "gene.b1588"
entity_type: "gene"
name: "ynfF"
source_database: "NCBI RefSeq"
source_id: "gene-b1588"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1588"
  - "ynfF"
---

# ynfF

`gene.b1588`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1588`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfF (gene.b1588) is a gene entity. It encodes ynfF (protein.P77783). Encoded protein function: FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}. EcoCyc product frame: G6846-MONOMER. Genomic coordinates: 1660556-1662979. EcoCyc protein note: YnfF has been implicated as a Tat-dependent selenate reductase enzyme in E.coli. A ynfEF double null mutant is unable to reduce selenate to elemental selenium . The disruption is specific to the initial selenate reduction process since selenium production is restored when selenite is added to the growth medium . Production of either YnfE or YnfF from a plasmid restored the ability of the E. coli ynfEF double mutant to reduce selenate to selenium in vivo . YnfF is highly similar to DmsA, the catalytic subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsA antibody. The protein is poorly expressed. When expressed together with DmsB and DmsC in a plasmid expression system, YnfF can form a complex with DmsB and DmsC, but the chimeric enzyme does not support growth on DMSO . The YnfF signal peptide can direct export through the twin arginine translocation (Tat) pathway and the general secretory pathway (Sec) pathway . YnfF is a predicted molybdoenzyme; deletion of ynfF does not confer a 6-N-hydroxylaminopurine (HAP)-sensitive phenotype .

## Biological Role

Repressed by narL (protein.P0AF28), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77783|protein.P77783]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ynfF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ynfF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ynfF; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ynfF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynfF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005307,ECOCYC:G6846,GeneID:945268`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1660556-1662979:+; feature_type=gene

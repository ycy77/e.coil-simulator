---
entity_id: "gene.b3366"
entity_type: "gene"
name: "nirD"
source_database: "NCBI RefSeq"
source_id: "gene-b3366"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3366"
  - "nirD"
---

# nirD

`gene.b3366`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3366`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nirD (gene.b3366) is a gene entity. It encodes nirD (protein.P0A9I8). Encoded protein function: FUNCTION: Required for activity of the reductase. {ECO:0000269|PubMed:1435259}. EcoCyc product frame: NIRD-MONOMER. Genomic coordinates: 3496551-3496877. EcoCyc protein note: NirD may be a subunit of the NADH-dependent nitrite reductase. Presence of nirD is required for nitrite reductase activity in cell extracts, and the NirD protein appears to be present in partially purified nitrite reductase . NirD interacts directly with NirB in a BACTH experiment . However, the function of NirD in enabling nitrite reductase activity has not been determined. NirD interacts directly with the catalytic domain of RELA-MONOMER RelA, thereby inhibiting the synthesis of (p)ppGpp and the stringent response. The E50K mutation eliminates the interaction with RelA, but does not affect the interaction with NirB . Overexpression of nirD leads to a decrease of the intracellular levels of (p)ppGpp . Expression of nirD is upregulated upon exposure to silver nanoparticles . NirD: "nitrite reductase"

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), cra (protein.P0ACP1). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9I8|protein.P0A9I8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nirD; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nirD; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nirD; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nirD; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nirD; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=nirD; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nirD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011005,ECOCYC:EG10655,GeneID:947881`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3496551-3496877:+; feature_type=gene

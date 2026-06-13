---
entity_id: "gene.b3511"
entity_type: "gene"
name: "hdeD"
source_database: "NCBI RefSeq"
source_id: "gene-b3511"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3511"
  - "hdeD"
---

# hdeD

`gene.b3511`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3511`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hdeD (gene.b3511) is a gene entity. It encodes hdeD (protein.P0AET5). Encoded protein function: Protein HdeD EcoCyc product frame: EG11495-MONOMER. EcoCyc synonyms: yhiA. Genomic coordinates: 3656995-3657567. EcoCyc protein note: HdeD is required for the acid resistance phenotype exhibited upon overproduction of G6789-MONOMER YdeO . An ΔhdeD null mutant appears to have no defect in the acid response , but when grown to later time points, it is in fact less sensitive to decreased pH than wild type . hdeD, yhiD, and gadE mutants have reduced viability at high cell density (~108 CFU per mL) at pH 2.1 compared to wild-type . High cell density-grown hdeD or gadE mutants are able to transiently protect wild-type cells grown at low cell density through the cell density dependent acid resistance mechanism, so HdeD and GadE are likely involved in receiving the protective signal, not sending it . HdeD is an inner membrane protein with six predicted transmembrane domains; its C terminus is located in the cytoplasm . HdeD is a heterogeneously expressed membrane protein . Expression of hdeD is derepressed in an hns deletion strain and is acid- and acetate-inducible . Transcription is negatively regulated by the TorS-TorR two-component signaling system and induced by overproduction of YdeO...

## Biological Role

Repressed by cyaR (gene.b4438), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoS (protein.P13445), phoP (protein.P23836), gadX (protein.P37639), gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AET5|protein.P0AET5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hdeD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=hdeD; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=hdeD; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=hdeD; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=hdeD; function=+
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=hdeD; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=hdeD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011467,ECOCYC:EG11495,GeneID:948024`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3656995-3657567:+; feature_type=gene

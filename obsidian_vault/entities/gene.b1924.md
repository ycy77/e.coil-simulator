---
entity_id: "gene.b1924"
entity_type: "gene"
name: "fliD"
source_database: "NCBI RefSeq"
source_id: "gene-b1924"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1924"
  - "fliD"
---

# fliD

`gene.b1924`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1924`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliD (gene.b1924) is a gene entity. It encodes fliD (protein.P24216). Encoded protein function: FUNCTION: Required for the morphogenesis and for the elongation of the flagellar filament by facilitating polymerization of the flagellin monomers at the tip of growing filament. Forms a capping structure, which prevents flagellin subunits (transported through the central channel of the flagellum) from leaking out without polymerization at the distal end. EcoCyc product frame: EG10841-MONOMER. EcoCyc synonyms: flbC, rfs. Genomic coordinates: 2003872-2005278. EcoCyc protein note: The filament cap lies at the distal, growing end of the flagellar filament and plays a critical role in the assembly of flagellin (FliC) monomers into the growing filament . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see

## Biological Role

Repressed by nac (protein.Q47005). Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24216|protein.P24216]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliD; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fliD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006407,ECOCYC:EG10841,GeneID:946428`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2003872-2005278:+; feature_type=gene

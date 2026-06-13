---
entity_id: "gene.b0758"
entity_type: "gene"
name: "galT"
source_database: "NCBI RefSeq"
source_id: "gene-b0758"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0758"
  - "galT"
---

# galT

`gene.b0758`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0758`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galT (gene.b0758) is a gene entity. It encodes galT (protein.P09148). Encoded protein function: Galactose-1-phosphate uridylyltransferase (Gal-1-P uridylyltransferase) (EC 2.7.7.12) (UDP-glucose--hexose-1-phosphate uridylyltransferase) EcoCyc product frame: GALACTURIDYLYLTRANS-MONOMER. EcoCyc synonyms: galB. Genomic coordinates: 789983-791029. EcoCyc protein note: Galactose 1-phosphate uridylyltransferase catalyzes an interconversion reaction in galactose catabolism. The overall equilibrium constant of the galactose-1-phosphate uridylyltransferase and UDP-galactose 4-epimerase reactions is 7.4, favoring glucose-1-phosphate formation . The reaction displays ping-pong bi-bi kinetics and a double displacement mechanism involving the formation of a uridylyl enzyme intermediate . The His166 residues acts as the nucleophile in the active site . The enzyme is a metalloenzyme containing both Zn2+ and Fe2+ . The ions appear to be structural rather than catalytic components . Only the Zn2+ binding site is essential for enzymatic activity . The enzyme shows an absolute requirement for cysteine . Crystal structures of the enzyme has been solved, allowing identification of the active site and understanding of substrate binding and catalytic mechanisms . The H164 and H166 residues are essential for enzymatic activity . A point mutation corresponding to Q168R in the E...

## Biological Role

Repressed by galR (protein.P03024), hns (protein.P0ACF8), crp (protein.P0ACJ8), galS (protein.P25748). Activated by rpoD (protein.P00579), galR (protein.P03024), crp (protein.P0ACJ8), rpoS (protein.P13445), galS (protein.P25748).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09148|protein.P09148]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=galT; function=+
- `activates` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galT; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galT; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=galT; function=+
- `activates` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galT; function=-+
- `represses` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galT; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=galT; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galT; function=-+
- `represses` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galT; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002573,ECOCYC:EG10366,GeneID:945357`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:789983-791029:-; feature_type=gene

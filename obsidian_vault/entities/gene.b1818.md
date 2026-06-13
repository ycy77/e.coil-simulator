---
entity_id: "gene.b1818"
entity_type: "gene"
name: "manY"
source_database: "NCBI RefSeq"
source_id: "gene-b1818"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1818"
  - "manY"
---

# manY

`gene.b1818`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1818`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

manY (gene.b1818) is a gene entity. It encodes manY (protein.P69801). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}. EcoCyc product frame: MANY-MONOMER. EcoCyc synonyms: pel, ptsP, ptsX. Genomic coordinates: 1903082-1903882. EcoCyc protein note: ManY is a hydrophobic integral membrane protein which together with ManZ forms the transmembrane channel of the E. coli ManXYZ mannose permease . ManY contains a PTS Enzyme IIC domain. The ManY and ManZ proteins alone are sufficient for penetration of λ phage DNA...

## Biological Role

Repressed by sgrS (gene.b4577). Activated by rpoD (protein.P00579), rpsA (protein.P0AG67).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69801|protein.P69801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=manY; function=+
- `activates` <-- [[protein.P0AG67|protein.P0AG67]] `RegulonDB|EcoCyc` `S` - regulator=RpsA; target=manY; function=+ | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=manY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006056,ECOCYC:EG10568,GeneID:946332`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1903082-1903882:+; feature_type=gene

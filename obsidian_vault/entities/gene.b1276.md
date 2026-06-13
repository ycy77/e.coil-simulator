---
entity_id: "gene.b1276"
entity_type: "gene"
name: "acnA"
source_database: "NCBI RefSeq"
source_id: "gene-b1276"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1276"
  - "acnA"
---

# acnA

`gene.b1276`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1276`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acnA (gene.b1276) is a gene entity. It encodes acnA (protein.P25516). Encoded protein function: FUNCTION: Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. The apo form of AcnA functions as a RNA-binding regulatory protein which plays a role as a maintenance or survival enzyme during nutritional or oxidative stress. During oxidative stress inactive AcnA apo-enzyme without iron sulfur clusters binds the acnA mRNA 3' UTRs (untranslated regions), stabilizes acnA mRNA and increases AcnA synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnA also enhances the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12486059, ECO:0000269|PubMed:1838390, ECO:0000269|PubMed:9421904}. EcoCyc product frame: ACONITASE-MONOMER. EcoCyc synonyms: acn. Genomic coordinates: 1335831-1338506. EcoCyc protein note: There are two aconitases in E. coli, both of which catalyze the reversible isomerization of citrate and iso-citrate via cis-aconitate. The apo form of AcnA is able to bind mRNA and enhances translation of AcnA . The AcnA enzyme is more stable, has a higher affinity for citrate and is active over a wider pH range than the AcnB enzyme . Unlike AcnB, AcnA is resistant to oxidation in vivo...

## Biological Role

Repressed by carbon storage regulator CsrA (complex.ecocyc.CPLX0-7956), csrA (protein.P69913). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), soxS (protein.P0A9E2), marA (protein.P0ACH5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25516|protein.P25516]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=acnA; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=acnA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=acnA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=acnA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7956|complex.ecocyc.CPLX0-7956]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=acnA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004283,ECOCYC:EG11325,GeneID:946724`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1335831-1338506:+; feature_type=gene

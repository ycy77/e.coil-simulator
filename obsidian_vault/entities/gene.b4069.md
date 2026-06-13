---
entity_id: "gene.b4069"
entity_type: "gene"
name: "acs"
source_database: "NCBI RefSeq"
source_id: "gene-b4069"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4069"
  - "acs"
---

# acs

`gene.b4069`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4069`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acs (gene.b4069) is a gene entity. It encodes acs (protein.P27550). Encoded protein function: FUNCTION: Catalyzes the conversion of acetate into acetyl-CoA (AcCoA), an essential intermediate at the junction of anabolic and catabolic pathways. Acs undergoes a two-step reaction. In the first half reaction, Acs combines acetate with ATP to form acetyl-adenylate (AcAMP) intermediate. In the second half reaction, it can then transfer the acetyl group from AcAMP to the sulfhydryl group of CoA, forming the product AcCoA.; FUNCTION: Enables the cell to use acetate during aerobic growth to generate energy via the TCA cycle, and biosynthetic compounds via the glyoxylate shunt. Acetylates CheY, the response regulator involved in flagellar movement and chemotaxis. EcoCyc product frame: ACS-MONOMER. EcoCyc synonyms: yfaC, acsA. Genomic coordinates: 4285413-4287371. EcoCyc protein note: Acetyl-CoA synthetase (Acs) activates acetate to acetyl-CoA in an ATP-dependent manner . Acs activity constitutes one of two distinct pathways by which E. coli activates acetate to acetyl-CoA. The Acs pathway (PWY0-1313) functions in a mainly anabolic role, scavenging acetate present in the extracellular medium. Induction of acs expression functions as the metabolic switch activating this pathway...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), fis (protein.P0A6R3), rob (protein.P0ACI0). Activated by crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27550|protein.P27550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=acs; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=acs; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=acs; function=-
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013337,ECOCYC:EG11448,GeneID:948572`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4285413-4287371:-; feature_type=gene

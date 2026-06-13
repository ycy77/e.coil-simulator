---
entity_id: "gene.b3620"
entity_type: "gene"
name: "waaF"
source_database: "NCBI RefSeq"
source_id: "gene-b3620"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3620"
  - "waaF"
---

# waaF

`gene.b3620`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3620`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaF (gene.b3620) is a gene entity. It encodes waaF (protein.P37692). Encoded protein function: FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112). Catalyzes the addition of the second heptose unit to the heptosyl-Kdo2-lipid A module (PubMed:11054112, PubMed:11717579). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose, but with lower efficiency (PubMed:11054112). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579}. EcoCyc product frame: EG12210-MONOMER. EcoCyc synonyms: rfaF. Genomic coordinates: 3794929-3795975. EcoCyc protein note: ADP-heptose:LPS heptosyltransferase II (HepII, WaaF) is the enzyme responsible for transfer of the second heptose sugar onto the heptosyl-Kdo2 moiety of the lipopolysaccharide inner core . A kinetic and biophysical characterization of HepII has been reported by . Truncation of the LPS inner core by defined mutations in hldD (rfaD), hldE (rfaE) or waaF resulted in high-level gab operon expression and a mucoid colony phenotype resulting from a colanic acid capsule . Production of colanic acid in the ΔwaaF mutant is dependent on the RcsCDB phosphorelay system . In waaC, waaE, waaF and waaG mutants, biofilm formation was significantly increased relative to the parental strain . A ΔwaaF strain lacks flagella...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37692|protein.P37692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaF; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=waaF; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=waaF; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=waaF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011845,ECOCYC:EG12210,GeneID:948135`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3794929-3795975:+; feature_type=gene

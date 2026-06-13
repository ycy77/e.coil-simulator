---
entity_id: "protein.P61714"
entity_type: "protein"
name: "ribE"
source_database: "UniProt"
source_id: "P61714"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribE ribH ybaF b0415 JW0405"
---

# ribE

`protein.P61714`

## Static

- Type: `protein`
- Source: `UniProt:P61714`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 6,7-dimethyl-8-ribityllumazine by condensation of 5-amino-6-(D-ribitylamino)uracil with 3,4-dihydroxy-2-butanone 4-phosphate. This is the penultimate step in the biosynthesis of riboflavin. {ECO:0000269|PubMed:8969176}. The ribE gene encodes lumazine synthase, an enzyme that catalyzes the penultimate step in the riboflavin biosynthesis pathway. The protein forms a hollow icosahedral capsid composed of 60 subunits. Unlike lumazine synthase from Bacillus subtilis, the E. coli enzyme is not physically associated with any other enzyme of the riboflavin biosynthetic pathway, including riboflavin synthase . ribE is an essential gene .

## Biological Role

Component of 6,7-dimethyl-8-ribityllumazine synthase (complex.ecocyc.LUMAZINESYN-CPLX).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of 6,7-dimethyl-8-ribityllumazine by condensation of 5-amino-6-(D-ribitylamino)uracil with 3,4-dihydroxy-2-butanone 4-phosphate. This is the penultimate step in the biosynthesis of riboflavin. {ECO:0000269|PubMed:8969176}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.LUMAZINESYN-CPLX|complex.ecocyc.LUMAZINESYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=60 | EcoCyc protcplxs.col coefficient=60

## Incoming Edges (1)

- `encodes` <-- [[gene.b0415|gene.b0415]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P61714`
- `KEGG:ecj:JW0405;eco:b0415;ecoc:C3026_02025;`
- `GeneID:946453;98391920;99810088;`
- `GO:GO:0000906; GO:0005737; GO:0005829; GO:0009231; GO:0009349`
- `EC:2.5.1.78`

## Notes

6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78)

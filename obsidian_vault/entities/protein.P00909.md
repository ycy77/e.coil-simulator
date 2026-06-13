---
entity_id: "protein.P00909"
entity_type: "protein"
name: "trpC"
source_database: "UniProt"
source_id: "P00909"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpC trpF b1262 JW1254"
---

# trpC

`protein.P00909`

## Static

- Type: `protein`
- Source: `UniProt:P00909`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional enzyme that catalyzes two sequential steps of tryptophan biosynthetic pathway. The first reaction is catalyzed by the isomerase, coded by the TrpF domain; the second reaction is catalyzed by the synthase, coded by the TrpC domain. Bifunctional phosphoribosylanthranilate isomerase / indole-3-glycerol phosphate synthase (TrpC) carries out the third and fourth steps in the tryptophan biosynthesis pathway. The phosphoribosylanthranilate isomerase activity of TrpC catalyzes the Amadori rearrangement of its substrate into carboxyphenylaminodeoxyribulose phosphate . The indole-glycerol phosphate synthase activity of TrpC catalyzes the ring closure of this product to yield indole-3-glycerol phosphate . Early mutant studies identified N-(5'-phosphoribosyl)-anthranilate (PRA) and 1-(o-carboxyphenylamino)-1'-deoxyribulose-5'-phosphate (CDRP) as intermediates in the biosynthesis of tryptophan and provided evidence that a single polypeptide chain catalyzes both the conversion of PRA to CDRP and CDRP to indole-3-glycerol-phosphate (IGP) . These observations were confirmed by kinetic and mutant complementation studies which further demonstrated that the two reactions occur at two distinct, non-overlapping sites on the polypeptide and that CDRP is a free intermediate...

## Biological Role

Catalyzes IGPSYN-RXN (reaction.ecocyc.IGPSYN-RXN), PRAISOM-RXN (reaction.ecocyc.PRAISOM-RXN).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Bifunctional enzyme that catalyzes two sequential steps of tryptophan biosynthetic pathway. The first reaction is catalyzed by the isomerase, coded by the TrpF domain; the second reaction is catalyzed by the synthase, coded by the TrpC domain.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.IGPSYN-RXN|reaction.ecocyc.IGPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PRAISOM-RXN|reaction.ecocyc.PRAISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1262|gene.b1262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00909`
- `KEGG:ecj:JW1254;eco:b1262;`
- `GeneID:945519;`
- `GO:GO:0000162; GO:0004425; GO:0004640`
- `EC:4.1.1.48; 5.3.1.24`

## Notes

Tryptophan biosynthesis protein TrpCF [Includes: Indole-3-glycerol phosphate synthase (IGPS) (EC 4.1.1.48); N-(5'-phospho-ribosyl)anthranilate isomerase (PRAI) (EC 5.3.1.24)]

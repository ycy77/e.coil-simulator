---
entity_id: "protein.P06983"
entity_type: "protein"
name: "hemC"
source_database: "UniProt"
source_id: "P06983"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemC popE b3805 JW5932"
---

# hemC

`protein.P06983`

## Static

- Type: `protein`
- Source: `UniProt:P06983`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Tetrapolymerization of the monopyrrole PBG into the hydroxymethylbilane pre-uroporphyrinogen in several discrete steps. {ECO:0000269|PubMed:3529035}. Hydroxymethylbilane synthase (HMBS) catalyzes the tetrapolymerization of porphobilinogen yielding the linear tetrapyrrole hydroxymethylbilane (preuroporphyrinogen) which is highly unstable. With uroporphyrinogen III synthase, the product cyclizes to the next intermediate, uroporphyrinogen III. In the absence of the next enzyme in the pathway, the product spontaneously cyclizes to form uroporphyrinogen I, which is not a normal metabolite. HMBS and uroporphyrinogen III synthase form a complex . HMBS contains a covalently bound dipyrromethane (dipyrrole) that is an essential cofactor for enzyme activity. The cofactor is bound irreversibly to cysteine-242 . The crystal structure of the enzyme has been determined up to 1.7 Å resolution . Site directed mutagenesis studies have been carried out in the catalytic cleft . Asp-84 has been shown to be a critical catalytic residue, substitution results in an almost inactive enzyme .

## Biological Role

Catalyzes porphobilinogen:(4-[2-carboxyethyl]-3-[carboxymethyl]pyrrol-2-yl)methyltransferase (hydrolysing); (reaction.R00084), OHMETHYLBILANESYN-RXN (reaction.ecocyc.OHMETHYLBILANESYN-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Tetrapolymerization of the monopyrrole PBG into the hydroxymethylbilane pre-uroporphyrinogen in several discrete steps. {ECO:0000269|PubMed:3529035}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00084|reaction.R00084]] `KEGG` `database` - via EC:2.5.1.61
- `catalyzes` --> [[reaction.ecocyc.OHMETHYLBILANESYN-RXN|reaction.ecocyc.OHMETHYLBILANESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3805|gene.b3805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06983`
- `KEGG:ecj:JW5932;eco:b3805;ecoc:C3026_20600;`
- `GeneID:947759;`
- `GO:GO:0004418; GO:0005737; GO:0005829; GO:0006782; GO:0006783; GO:0033014`
- `EC:2.5.1.61`

## Notes

Porphobilinogen deaminase (PBG) (EC 2.5.1.61) (Hydroxymethylbilane synthase) (HMBS) (Pre-uroporphyrinogen synthase)
